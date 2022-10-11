from django.core.paginator import Paginator
from django.db.models import Count
from django.shortcuts import render
from catalog_app.models import Post, Media
from category_app.models import Tag


def get_tags(request, title):
    """Представление товаров по категориям"""

    posts = Post.objects.filter(tag__title=title).order_by('-id').all()

    paginator = Paginator(posts, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    tag = Tag.objects.annotate(count=Count("post")).order_by("-count")[:5]

    image_post = []

    for post in posts:
        image_post.append(Media.objects.filter(post=post).first())

    tags = Tag.objects.get(title=title)

    return render(request, 'tag.html', {
        'posts': posts,
        'image_post': image_post,
        'tag': tag,
        'tags': tags,
        'page_obj': page_obj,
    })