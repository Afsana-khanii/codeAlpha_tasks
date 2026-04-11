from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_user, name='login'),
    path('register/', views.register, name='register'),
    path('home', views.home, name='home'),
    path('product/<int:id>/', views.product_detail, name='product_detail'),
    
    
    path('logout/', views.logout_user, name='logout'),
    path('cart/', views.view_cart, name='cart'),
path('add_to_cart/<int:id>/', views.add_to_cart, name='add_to_cart'),
 path('remove_from_cart/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
path('checkout/', views.checkout, name='checkout'),
]