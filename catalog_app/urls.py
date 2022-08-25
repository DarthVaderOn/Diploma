from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from catalog_app.views.catalog import CatalogPageView
from catalog_app.views.main import MainPageView
from catalog_app.views.my_catalog import MyPosts
from catalog_app.views.create_ad import PostCreate


urlpatterns = [
    path('', login_required(MainPageView.as_view()), name='main_page'),
    path('myposts', login_required(MyPosts.as_view()), name='my_post'),
    path('tag/<str:title>/', login_required(MainPageView.get_tags), name='get_tags'),
    path('create_ad', login_required(PostCreate.as_view()), name='post_page'),
    path('catalog', login_required(CatalogPageView.as_view()), name='catalog_page'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()