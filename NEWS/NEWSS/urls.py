from rest_framework import routers
from .views import NewsViewSet,ThemeViewSet

router = routers.DefaultRouter()
router.register('api/news', NewsViewSet, 'news')
router.register('api/themes', ThemeViewSet, 'Themes')


urlpatterns = router.urls

