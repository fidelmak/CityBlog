from django import forms
from .models import Comment, New

class CommentForm(forms.ModelForm):
    class Meta:
        model= Comment
        exclude = ["post"]
        labels = {
            "user_name": "your Name",
            "user_email": "Your Email",
            "text": "Your Comment"

        }

class NewForm(forms.ModelForm):
    class Meta:
        model= New
        exclude = ["post"]
        labels = {
            "user_name": "your Name",
            "image": "image",
            "text": "Your Comment"

        }


