from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse

from catalog_app.models import Post


@login_required
def add_to_favorites(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if post.favorite_product.filter(user=request.user.id).exists():
        post.favorite_product.append(post.favorite_product.pk)
    else:
        None
    post.save()
    return redirect(reverse('main_page'))