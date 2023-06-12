from rest_framework import routers
from .api import MenuViewSet
from django.conf import settings
from django.conf.urls.static import static


router = routers.DefaultRouter()
router.register('', MenuViewSet, 'menu')


urlpatterns = router.urls


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)