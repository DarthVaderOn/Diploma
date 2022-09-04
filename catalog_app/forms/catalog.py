from django import forms
from catalog_app.models import Post


class PostForm(forms.ModelForm):
    """Класс формы постов"""
    class Meta:
        model = Post
        fields = ['title', 'text', 'is_public','tag', 'year', 'price', 'country']
        widget = {
            'title': forms.TextInput(),
            'text': forms.TextInput(),
            'is_public': forms.BooleanField(initial=True),
        }


class AddImagePost(PostForm):
    """Класс формы изображений к постам"""
    image = forms.ImageField(
        required=False,
        widget=forms.FileInput(attrs={'multiple': True})
    )


    class Meta(PostForm.Meta):
        fields = PostForm.Meta.fields + ["image", ]