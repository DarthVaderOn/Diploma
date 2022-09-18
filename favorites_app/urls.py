from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include
from favorites_app.api.views.router import api_router
from favorites_app.views.favorites import add_to_favorites


urlpatterns = [
    path('favorites/<int:post_id>', add_to_favorites, name='add_to_favorites'),
    path('api/', include(api_router.urls)),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()