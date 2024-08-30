from django import forms
from django.core.mail import send_mail

from .models import Post, Comment


class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25, label="Your name")
    to = forms.EmailField(label="Share to")
    comments = forms.CharField(required=False, widget=forms.Textarea)


class CommentForm(forms.ModelForm):
    parent = forms.IntegerField(widget=forms.HiddenInput, required=False)

    class Meta:
        model = Comment
        fields = ("body",)
        labels = {
            "body": "Your comment",
        }
        widgets = {
            "body": forms.Textarea(attrs={"rows": 3}),
        }

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if not self.user or not self.user.is_authenticated:
            self.fields['name'] = forms.CharField(max_length=80, required=True)
            self.fields['email'] = forms.EmailField(required=True)


class SearchForm(forms.Form):
    query = forms.CharField(label='', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Search for posts...',
        'aria-label': 'Search',
    }))
