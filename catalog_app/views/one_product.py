from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.views import View
from catalog_app.models import Post, Media
from review_app.forms.review import AddImageReview
from review_app.models import MediaReview, Review


class ProductView(View):
    """Полное описание товара и отзывов к нему, последние просмотренные товары """
    def get(self, request, pk):
        one_product = Post.objects.get(id=pk)
        image_post = Media.objects.filter(post=one_product)
        reviews = Review.objects.order_by("-created_at").filter(post=one_product).all()

        paginator = Paginator(reviews, 2)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        rating = 0
        for review in reviews:
            rating += review.rating
        if rating > 0:
            rating = round(rating/len(reviews), 1)

        form = AddImageReview()

        media_post = []
        if 'recently_viewed' in request.session:
            if pk in request.session['recently_viewed']:
                request.session['recently_viewed'].remove(pk)

            recently_viewed_post = Post.objects.filter(pk__in=request.session['recently_viewed'])
            request.session['recently_viewed'].insert(0, pk)
            if len(request.session['recently_viewed']) > 5:
                request.session['recently_viewed'].pop()

            for post in recently_viewed_post:
                media_post.append(post.media_post.first())
        else:
            request.session['recently_viewed'] = [pk]
        request.session.modified = True

        return render(request, "one_product.html", {
            'one_product': one_product,
            'image_post': image_post,
            'reviews': reviews,
            "rating": rating,
            'form': form,
            'recently_viewed_post': media_post,
            'page_obj': page_obj,
        })


    def post(self, request, pk):
        """Добавление отзыва"""
        form = AddImageReview(request.POST, request.FILES)
        files = request.FILES.getlist('image')
        one_product = Post.objects.get(id=pk)
        image_post = Media.objects.filter(post=one_product)
        reviews = Review.objects.order_by("-created_at").filter(post=one_product)

        paginator = Paginator(reviews, 2)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        rating = 0
        for review in reviews:
            rating += review.rating
        if rating > 0:
            rating = round(rating / len(reviews), 1)

        media_post = []
        if 'recently_viewed' in request.session:
            if pk in request.session['recently_viewed']:
                request.session['recently_viewed'].remove(pk)

            recently_viewed_post = Post.objects.filter(pk__in=request.session['recently_viewed'])
            request.session['recently_viewed'].insert(0, pk)
            if len(request.session['recently_viewed']) > 5:
                request.session['recently_viewed'].pop()

            for post in recently_viewed_post:
                media_post.append(post.media_post.first())
        else:
            request.session['recently_viewed'] = [pk]
        request.session.modified = True

        if Review.objects.filter(post=one_product).filter(user=request.user).exists():
            return render(request, 'one_product.html', context={
                'one_product': one_product,
                'image_post': image_post,
                'reviews': reviews,
                "rating": rating,
                'form': form,
                'recently_viewed_post': media_post,
                'page_obj': page_obj,
                'error': 'You have left a review before!'
            })

        if len(files) > 5:
            return render(request, 'one_product.html', context={
                'one_product': one_product,
                'image_post': image_post,
                'reviews': reviews,
                'form': form,
                'recently_viewed_post': media_post,
                'page_obj': page_obj,
                'error': 'Image upload error: Allowed upload limit is no more than 5 files!'
            })

        if form.is_valid():
            post_object = Review.objects.create(user=request.user, text=form.cleaned_data['text'], rating=form.cleaned_data['rating'], ip=request.META.get('REMOTE_ADDR') , post=one_product)
            for f in files:
                MediaReview.objects.create(review=post_object, image_review=f)
            return redirect(f"/catalog/{pk}")