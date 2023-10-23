from rest_framework import serializers
from .models import Section

class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = ['name','slug','image']


class GameSerailizer(serializers.ModelSerializer):
    pass
