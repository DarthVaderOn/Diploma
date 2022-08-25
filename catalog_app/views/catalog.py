from django.db.models import Count
from django.shortcuts import render
from django.views import View
from catalog_app.models import Media
from catalog_app.models import Post
from category_app.models import Tag


class CatalogPageView(View):
    """Класс представление главной страницы"""

    def get(self, request):
        """Представление постов"""

        posts = Post.objects.all()

        if posts:

            tag = Tag.objects.annotate(count=Count("post")).order_by("-count")[:5]
            image_post = Media.objects.all()
            contex = {'title': 'Hello World!',
                      'posts': posts,
                      'image_post': image_post,
                      'tag': tag,
                      }
        else:
            contex = {'title': 'Hello World!',
                      'error': "Oops, this item may have been removed =/",
                      }

        return render(request, 'all_catalog.html', contex)