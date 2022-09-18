from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from datetime import datetime
from catalog_app.models import Post, Media
from review_app.forms.review import AddImageReview
from review_app.models import MediaReview, Review


class ProductView(View):
    """Полное описание товара и отзывов к нему"""
    def get(self, request, pk):
        post = get_object_or_404(Post, id=pk)
        post.last_visit = datetime.now()
        post.save()
        one_product = Post.objects.get(id=pk)
        image_post = Media.objects.filter(post=one_product)
        review = Review.objects.order_by("-created_at").filter(post=one_product)
        form = AddImageReview()
        return render(request, "one_product.html", {
            'one_product': one_product,
            'image_post': image_post,
            'reviews': review,
            'form': form
        })


    def post(self, request, pk):
        """Добавление отзыва"""
        form = AddImageReview(request.POST, request.FILES)
        files = request.FILES.getlist('image')
        one_product = Post.objects.get(id=pk)
        image_post = Media.objects.filter(post=one_product)
        review = Review.objects.order_by("-created_at").filter(post=one_product)

        if len(files) > 5:
            return render(request, 'one_product.html', context={
                'one_product': one_product,
                'image_post': image_post,
                'reviews': review,
                'form': form,
                'error': 'Image upload error: Allowed upload limit is no more than 5 files!'
            })

        if form.is_valid():
            post_object = Review.objects.create(user=request.user, text=form.cleaned_data['text'], post=one_product)
            for f in files:
                MediaReview.objects.create(review=post_object, image_review=f)
            return redirect(f"/catalog/{pk}")