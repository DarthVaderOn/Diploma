from django.shortcuts import render
from django.views import View
from catalog_app.models import Post, Media


class ProductView(View):
    """Полное описание товара"""
    def get(self, request, pk):
        one_product = Post.objects.get(id=pk)
        image_post = Media.objects.all()
        return render(request, "one_product.html", {
            'one_product': one_product,
            'image_post': image_post
        })