from django.utils import timezone
from django.core.paginator import Paginator
from django.db.models import Count
from django.shortcuts import render
from django.views import View
from catalog_app.models import Post, Media
from category_app.models import Tag


class LastProductView(View):
    """Полное описание товара и отзывов к нему"""

    def get(self, request):
        """Представление постов"""

        posts = Post.objects.filter(last_visit__date=timezone.now()).order_by('-last_visit')
        paginator = Paginator(posts, 5)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        if posts:

            tag = Tag.objects.annotate(count=Count("post")).order_by("-count")[:5]
            image_post = Media.objects.all()
            contex = {'title': 'Last Visit',
                      'posts': posts,
                      'image_post': image_post,
                      'tag': tag,
                      'page_obj': page_obj,
                      }
        else:
            contex = {'title': 'Last Visit',
                      'error': "Oops, you didn't view any products ¯\_(ツ)_/¯ ",
                      }
        return render(request, 'last_visit.html', contex)