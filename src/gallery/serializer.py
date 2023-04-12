from rest_framework import serializers
from .models import photo, gallery


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = photo
        fields = ['id', 'filename', 'description', 'edit_date']


class SimpleGallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = gallery
        fields = ['id', 'name']


class GallerySerializer(serializers.ModelSerializer):
    photos = PhotoSerializer

    class Meta:
        model = gallery
        fields = ['id', 'name', 'description', 'sort_value', 'edit_date', 'photos']

