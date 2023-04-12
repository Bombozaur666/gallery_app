from rest_framework import serializers
from .models import subjects


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = subjects
        fields = ['id', 'name', 'row_id', 'row_prefix']
