from django import forms
from review_app.models import Review


class ReviewForm(forms.ModelForm):
    """Класс формы отзывов"""
    class Meta:
        model = Review
        fields = ["rating", "text"]
        widgets = {
            "text": forms.TextInput(),
            "user": forms.HiddenInput(),
            "post": forms.HiddenInput(),
            'rating': forms.NumberInput(attrs={'class': 'Stars'})

        }
        labels = {'rating': 'Enter Rating 1 to 5'}


class AddImageReview(ReviewForm):
    """Класс формы изображений к отзывам"""
    image = forms.ImageField(
        required=False,
        widget=forms.FileInput(attrs={'multiple': True})
    )


    class Meta(ReviewForm.Meta):
        fields = ReviewForm.Meta.fields + ["image", ]