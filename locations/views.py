from rest_framework import viewsets,filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Location, LocationImage, Facility, Category
from .serializers import (
    LocationSerializer,
    LocationImageSerializer,
    FacilitySerializer,
    CategorySerializer
)
from .permissions import IsAdminOrReadOnly 

class FacilityViewSet(viewsets.ModelViewSet):
    queryset = Facility.objects.all()
    serializer_class = FacilitySerializer
    permission_classes = [IsAdminOrReadOnly]

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrReadOnly]

class LocationImageViewSet(viewsets.ModelViewSet):
    queryset = LocationImage.objects.all()
    serializer_class = LocationImageSerializer
    permission_classes = [IsAdminOrReadOnly]


class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    # permission_classes = [IsAdminOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]

    filterset_fields = ['price', 'rating', 'facilities', 'categories']
    search_fields = ['title', 'description', 'location']

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
