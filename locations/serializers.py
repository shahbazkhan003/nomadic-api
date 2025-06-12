from rest_framework import serializers
from .models import Location, LocationImage, Facility, Category


class FacilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Facility
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class LocationImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocationImage
        fields = '__all__'

class LocationSerializer(serializers.ModelSerializer):
    facilities = serializers.PrimaryKeyRelatedField(queryset=Facility.objects.all(), many=True)
    categories = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), many=True)
    images = LocationImageSerializer(many=True, read_only=True)

    class Meta:
        model = Location
        fields = [
            'id', 'title', 'description', 'location',
            'rating', 'price', 'facilities', 'categories', 'images'
        ]
        read_only_fields = ['user']  
