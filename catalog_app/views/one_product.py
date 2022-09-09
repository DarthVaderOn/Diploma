from django.shortcuts import render, redirect
from django.views import View
from catalog_app.models import Post, Media
from review_app.form.review import AddImageReview
from review_app.models import MediaReview, Review


class ProductView(View):
    """Полное описание товара"""
    def get(self, request, pk):
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