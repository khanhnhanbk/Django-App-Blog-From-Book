from django.contrib import admin
from .models import Post, Comment
from django import forms

class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'tinymce'}))

    class Meta:
        model = Post
        fields = '__all__'

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm
    list_display = ["title", "slug", "author", "publish", "status"]
    list_filter = ["status", "created", "publish", "author"]
    search_fields = ["title", "content"]
    prepopulated_fields = {"slug": ("title",)}
    raw_id_fields = ["author"]
    date_hierarchy = "publish"
    ordering = ["status", "publish"]
    show_facets = admin.ShowFacets.ALWAYS

    class Media:
        js = ('tinymce/tinymce.min.js',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "post", "created", "active"]
    list_filter = ["active", "created", "updated"]
    search_fields = ["name", "email", "body"]
