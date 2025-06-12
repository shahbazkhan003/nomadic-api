from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LocationViewSet, LocationImageViewSet, FacilityViewSet, CategoryViewSet

router = DefaultRouter()
router.register(r'locations', LocationViewSet)
router.register(r'images', LocationImageViewSet)
router.register(r'facilities', FacilityViewSet)
router.register(r'categories', CategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
