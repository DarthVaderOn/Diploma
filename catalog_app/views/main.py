from django.core.paginator import Paginator
from django.db.models import Count
from django.shortcuts import render
from django.views import View
from favorites_app.models import FavoriteProduct
from catalog_app.models import Media
from catalog_app.models import Post
from category_app.models import Tag


class MainPageView(View):
    """Главная страница"""

    def get(self, request):
        """Представление избранных товаров"""

        basket = FavoriteProduct.objects.filter(user=request.user.pk)

        favorite_product = []

        for post in basket:

            if post.favorite_product.pk not in favorite_product:
                favorite_product.append(post.favorite_product.pk)

        if basket:

            posts = Post.objects.filter(is_public=True).filter(id__in=favorite_product).all()
            paginator = Paginator(posts, 3)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)

            if posts:

                tag = Tag.objects.annotate(count=Count("post")).order_by("-count")[:5]
                image_post = Media.objects.all()
                contex =  {'posts': posts,
                          'image_post': image_post,
                          'tag': tag,
                          'page_obj': page_obj,
                          }
            else:
                contex = {'error': "Oops, this item may have been removed =/",
                          }
        else:
            contex = {'error': "Oops. You don't have favorite items. Time to change that :)",
                      }

        return render(request, 'main_page.html', contex)


    def get_tags(request, title):
        """Представление тегов"""

        posts = Post.objects.filter(tag__title=title).order_by('-id').all()
        paginator = Paginator(posts, 2)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        tag = Tag.objects.annotate(count=Count("post")).order_by("-count")[:5]
        image_post = Media.objects.all()
        tags = Tag.objects.get(title=title)
        return render(request, 'category.html', {
            'title': 'Categories',
            'posts': posts,
            'image_post': image_post,
            'tag': tag,
            'tags': tags,
            'page_obj': page_obj,
        })