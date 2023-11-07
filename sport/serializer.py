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

class TeamListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['name','slug','image']   

class TeamDetailSerializer(serializers.ModelSerializer):
    players = PlayerSerializer(many = True)
    class Meta:
        model = Team
        fields = ['name','slug','image','players']
 
class GameListSerailizer(serializers.ModelSerializer):
    team1 = TeamListSerializer()
    team2 = TeamListSerializer()
    class Meta:
        model = Game
        fields = ['team1','team2','win','draw','lose']

class GameDetailSerailizer(serializers.ModelSerializer):
    # section = SectionSerializer()
    team1 = TeamDetailSerializer()
    team2 = TeamDetailSerializer()
    class Meta:
        model = Game
        fields = ['team1','team2','win','draw','lose'] # 'section',
