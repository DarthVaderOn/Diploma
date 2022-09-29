from django.core.paginator import Paginator
from django.db.models import Count
from django.shortcuts import render
from django.views import View
from catalog_app.models import Media
from catalog_app.models import Post
from category_app.models import Tag


class CatalogPageView(View):
    """Каталог товаров"""

    def get(self, request):
        """Представление каталога товаров"""

        posts = Post.objects.filter(is_public=True).order_by('-created_at')

        paginator = Paginator(posts, 5)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        if posts:

            tag = Tag.objects.annotate(count=Count("post")).order_by("-count")[:5]
            image_post = []
            for post in posts:
                image_post.append(Media.objects.filter(post=post).first)
            contex = {
                      "posts": posts,
                      "image_post": image_post,
                      "tag": tag,
                      "page_obj": page_obj,
                      }
        else:
            contex = {
                      "error": "Oops, this item may have been removed =/",
                      }
        return render(request, 'all_catalog.html', contex)