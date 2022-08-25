from user_app.models import User
from django.db.models import Count
from django.shortcuts import render
from django.views import View
from catalog_app.models import Media
from catalog_app.models import Post
from category_app.models import Tag


class MyPosts(View):
    """Класс представление ваших записей"""

    def get(self, request):
        """Представление постов"""

        user_id = User.objects.filter(profile=request.user.profile.pk)

        user_post = []

        for user in user_id:

            if user.pk not in user_post:
                user_post.append(user.pk)

        if user_id:

            posts = Post.objects.filter(is_public=True).filter(user_id__in=user_post).all()

            if posts:

                tag = Tag.objects.annotate(count=Count("post")).order_by("-count")[:5]
                image_post = Media.objects.all()

                contex = {'title': 'My Posts!',
                          'posts': posts,
                          'image_post': image_post,
                          'tag': tag,
                          }
            else:
                contex = {'title': 'My Posts!',
                          'error': "You don't have any ads yet. Create your first ad."
                          }

        return render(request, 'my_catalogs.html', contex)


    def get_tags(self, request, tag_id):
        """Представление тегов"""

        posts = Post.objects.filter(is_public=True).all()
        tag = Tag.objects.annotate(count=Count("post")).order_by("-count")[:5]
        image_post = Media.objects.all()
        tags = Tag.objects.get(pk=tag_id)
        return render(request, 'tag.html', {
            'title': 'Categories',
            'posts': posts,
            'image_post': image_post,
            'tag': tag,
            'tags': tags,
        })