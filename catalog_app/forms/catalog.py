from django import forms
from catalog_app.models import Post


class PostForm(forms.ModelForm):
    """Форма создания продукта"""
    class Meta:
        model = Post
        fields = ['title', 'text', 'tag', 'year', 'price', 'country', 'is_public',]
        widget = {
            'title': forms.TextInput(),
            'text': forms.TextInput(),
            'is_public': forms.BooleanField(initial=True),
            'price': forms.TextInput(),
        }


class AddImagePost(PostForm):
    """Класс формы изображений к постам"""
    
    image = forms.ImageField(
        required=True,
        widget=forms.FileInput(attrs={'multiple': True})
    )


    class Meta(PostForm.Meta):
        fields = PostForm.Meta.fields + ["image", ]