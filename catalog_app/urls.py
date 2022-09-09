from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include
from catalog_app.api.views.router import api_router
from catalog_app.views.catalog import CatalogPageView
from catalog_app.views.main import MainPageView
from catalog_app.views.create_ad import PostCreate
from catalog_app.views.one_product import ProductView


urlpatterns = [
    path('', login_required(MainPageView.as_view()), name='main_page'),
    path('create_ad', login_required(PostCreate.as_view()), name='post_page'),
    path('catalog', login_required(CatalogPageView.as_view()), name='catalog_page'),
    path('tag/<str:title>/', login_required(MainPageView.get_tags), name='get_tags'),
    path("catalog/<int:pk>/", login_required(ProductView.as_view()), name='product_single'),
    path('api/', include(api_router.urls)),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()