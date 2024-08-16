from django import forms
from django.core.mail import send_mail

from .models import Post, Comment


class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25, label="Your name")
    to = forms.EmailField(label="Share to")
    comments = forms.CharField(required=False, widget=forms.Textarea)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["name", "email", "body"]
        labels = {
            "name": "Your name",
            "email": "Your email",
            "body": "Your comment",
        }
