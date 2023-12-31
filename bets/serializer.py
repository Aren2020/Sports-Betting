from rest_framework import serializers
from sport.serializer import GameListSerializer
from .models import Bets

class BetListSerializer(serializers.ModelSerializer):
    game = GameListSerializer()
    class Meta:
        model = Bets
        fields = ['game', 'amount', 'user_choice', 'win_choice']

    