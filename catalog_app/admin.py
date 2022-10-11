from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from django.contrib import admin
from django.utils.safestring import mark_safe
from catalog_app.models import Media, Post


# Register your models here.


class PostAdminForm(forms.ModelForm):
    text = forms.CharField(label="Description", widget=CKEditorUploadingWidget())
    class Meta:
        model = Post
        fields = '__all__'


class MediaProductAdmin(admin.StackedInline):
    """Вывод изображений товаров в админке"""
    model = Media
    list_display = ('image_post','preview')
    readonly_fields = ('image_post','preview')
    extra = 1


    def preview(self, obj):
        """Превью при нажатии на картинку"""
        if obj.image_post:
            return mark_safe(
                f'<a target=_blank href={obj.image_post.url}>'
                f'<img src={obj.image_post.url} width="100" height="100">'
                f'</a>'
            )
        else:
            return 'No Image'


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Вывод товаров с изображениями и настойки админки"""
    inlines = (
        MediaProductAdmin,
    )
    list_display = ('id', 'title', 'user', 'tag', 'created_at', 'is_public',)
    list_display_links = ('title',)
    list_filter = ('id', 'user', 'tag', 'created_at', 'is_public',)
    ordering = ('-created_at', 'id',)
    readonly_fields = ('created_at',)
    list_editable = ('is_public', 'tag', 'user',)
    search_fields = ('title', 'text', 'user__username')
    form = PostAdminForm
    save_on_top = True