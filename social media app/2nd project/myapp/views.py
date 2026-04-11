from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Post, Comment, Like, Follow, Profile
from .forms import PostForm, CommentForm


@login_required
def home(request):
    posts = Post.objects.all().order_by('-created_at')
    comment_form = CommentForm()
    return render(request, 'home.html', {
        'posts': posts,
        'comment_form': comment_form
    })



@login_required
def profile(request, username):
    user_obj = get_object_or_404(User, username=username)
    posts = Post.objects.filter(user=user_obj)

    is_following = Follow.objects.filter(
        follower=request.user, following=user_obj
    ).exists()

    followers_count = Follow.objects.filter(following=user_obj).count()
    following_count = Follow.objects.filter(follower=user_obj).count()

    return render(request, 'profile.html', {
        'user_obj': user_obj,
        'posts': posts,
        'is_following': is_following,
        'followers_count': followers_count,
        'following_count': following_count,
    })


@login_required
def create_post(request):
    form = PostForm()

    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('home')

    return render(request, 'create_post.html', {'form': form})



@login_required
def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    like, created = Like.objects.get_or_create(
        user=request.user,
        post=post
    )

    if not created:
        like.delete() 
    return redirect('home')



@login_required
def add_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()

    return redirect('home')



@login_required
def follow_user(request, username):
    user_to_follow = get_object_or_404(User, username=username)

    follow, created = Follow.objects.get_or_create(
        follower=request.user,
        following=user_to_follow
    )

    if not created:
        follow.delete()  

    return redirect('profile', username=username)