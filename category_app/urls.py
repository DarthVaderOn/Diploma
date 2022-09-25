from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include
from category_app.api.views.router import api_router
from category_app.views.category import get_tags
from favorites_app.views.main import MainPageView


urlpatterns = [
    path('api/', include(api_router.urls)),
    path('', login_required(MainPageView.as_view()), name='main_page'),
    path('tag/<str:title>/', login_required(get_tags), name='get_tags'),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()