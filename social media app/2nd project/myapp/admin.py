from django.contrib import admin
from .models import Profile, Post, Comment, Like, Follow 
# Register your models here.


admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(Follow)