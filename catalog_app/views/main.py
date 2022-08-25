from django.db.models import Count
from django.shortcuts import render
from django.views import View
from favorites_app.models import FollowRequest
from catalog_app.models import Media
from catalog_app.models import Post
from category_app.models import Tag


class MainPageView(View):
    """Класс представление главной страницы"""

    def get(self, request):
        """Представление постов"""

        subscriber = FollowRequest.objects.filter(user=request.user.pk)

        users_follow = []

        for users in subscriber:

            if users.user_follow.pk not in users_follow:
                users_follow.append(users.user_follow.pk)

        if subscriber:

            posts = Post.objects.filter(is_public=True).filter(user_id__in=users_follow).all()

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
        else:
            contex = {'title': 'Hello World!',
                      'error': "Oops. You don't have favorite items. Time to change that :)",
                      }

        return render(request, 'main_page.html', contex)


    def get_tags(request, title):
        """Представление тегов"""

        posts = Post.objects.filter(tag__title=title).order_by('-id').all()
        tag = Tag.objects.annotate(count=Count("post")).order_by("-count")[:5]
        image_post = Media.objects.all()
        tags = Tag.objects.get(title=title)
        return render(request, 'category.html', {
            'title': 'Categories',
            'posts': posts,
            'image_post': image_post,
            'tag': tag,
            'tags': tags,
        })