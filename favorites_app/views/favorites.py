from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from catalog_app.models import Post
from favorites_app.models import FavoriteProduct


@login_required
def add_to_favorites(request, post_id):
    """Добавление товара в избранное"""

    post = get_object_or_404(Post, id=post_id)
    if not FavoriteProduct.objects.filter(user=request.user, favorite_product=post).exists():
        FavoriteProduct.objects.create(user=request.user, favorite_product=post)

    return redirect(f"/catalog/{post_id}")


@login_required
def delete_to_favorites(request, post_id):
    """Удаление товара из избранного"""

    post = get_object_or_404(Post, id=post_id)
    a = FavoriteProduct.objects.filter(user=request.user, favorite_product=post)
    print(a)
    if a.exists():
        a.delete()

    return redirect(f"/catalog/{post_id}")