from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from .forms import RegisterForm
from .models import Product, Order, OrderItem



def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('login')



def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})

def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'product_detail.html', {'product': product})

def add_to_cart(request, id):
    cart = request.session.get('cart', {})
    cart[str(id)] = cart.get(str(id), 0) + 1
    request.session['cart'] = cart
    return redirect('home')

def view_cart(request):
    cart = request.session.get('cart', {})
    products = Product.objects.filter(id__in=cart.keys())
    cart_items = []
    total_price = 0
    for product in products:
        quantity = cart[str(product.id)]
        total = product.price * quantity
        total_price += total
        cart_items.append({
            'product': product,
            'quantity': quantity,
            'total': total
        })
    return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price})




def checkout(request):
    if not request.user.is_authenticated:
        return redirect('login')

    cart = request.session.get('cart', {})
    if not cart:
        return redirect('home')  

    order = Order.objects.create(user=request.user)
    for product_id, qty in cart.items():
        product = Product.objects.get(id=product_id)
        OrderItem.objects.create(order=order, product=product, quantity=qty)
    order.complete = True
    order.save()

    request.session['cart'] = {}  
    return render(request, 'order_success.html', {'order': order})

    from django.shortcuts import redirect, get_object_or_404

def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})
    
    product_id_str = str(product_id)  
    if product_id_str in cart:
        del cart[product_id_str] 
        request.session['cart'] = cart 
    
    return redirect('cart')  