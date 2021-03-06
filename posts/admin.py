from django import forms
from django.utils import timezone
from django.contrib import admin

from ckeditor_uploader.widgets import CKEditorUploadingWidget

from .models import Post, Tag


class PostAdminForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('author', 'created_at', 'updated_at', 'published_at')
        widgets = {
            'body': CKEditorUploadingWidget(),
            'snippet': CKEditorUploadingWidget(config_name='small'),
        }


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at', 'published_at', 'author']
    date_hierarchy = 'created_at'
    list_filter = ('created_at', 'status')
    search_fields = ['title']

    form = PostAdminForm
    prepopulated_fields = {'slug': ('title',)}

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        if (obj.published_at is None
                and obj.status in [Post.STATUS_PUBLISHED, Post.STATUS_ARCHIVED]):
            obj.published_at = timezone.now()
        if change:
            obj.updated_at = timezone.now()
        super(PostAdmin, self).save_model(request, obj, form, change)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}