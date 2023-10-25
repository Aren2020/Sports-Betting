from rest_framework import serializers
from .models import Section, Game, Team, Player

class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = ['name','slug','image']

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ['name','slug','image']

class TeamSerializer(serializers.ModelSerializer):
    players = PlayerSerializer(many = True)
    class Meta:
        model = Team
        fields = ['name','slug','image','players']

class GameSerailizer(serializers.ModelSerializer):
    section = SectionSerializer()
    team1 = TeamSerializer()
    team2 = TeamSerializer()
    class Meta:
        model = Game
        fields = ['section','team1','team2','win','draw','lose']
