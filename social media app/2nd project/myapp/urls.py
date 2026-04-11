from django.urls import path
from . import views

urlpatterns = [
    path('profile/<str:username>/', views.profile, name='profile'),
    path('', views.home, name='home'),
    
    path('create/', views.create_post, name='create_post'),
    path('like/<int:post_id>/', views.like_post, name='like_post'),
    path('comment/<int:post_id>/', views.add_comment, name='add_comment'),
    path('follow/<str:username>/', views.follow_user, name='follow_user'),
]