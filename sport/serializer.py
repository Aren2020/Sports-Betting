from rest_framework import serializers
from .models import SportSection

class SportSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SportSection
        fields = ['name','slug','image']

