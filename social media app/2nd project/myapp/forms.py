from django import forms

from .models import Post, Comment, Profile



class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content', 'image']



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'profile_pic']