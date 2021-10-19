from django import forms
from .models import Comment, Post
from blog import models

class CommentForm(forms.ModelForm):
    class Meta:
        model= Comment
        exclude = ["post"]
        #fields=["__all__"]
        labels = {
            "user_name":"Your Name",
            "user_email":"Your Email",
            "text":"Your Comment",
        }
