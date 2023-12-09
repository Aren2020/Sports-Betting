from rest_framework import serializers
from .models import Section, Game, Team, Player, News

class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = ['name']

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ['name','image','position']

class TeamListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['name','image']   

class TeamDetailSerializer(serializers.ModelSerializer):
    players = PlayerSerializer(many = True)
    class Meta:
        model = Team
        fields = ['name','image','players']
 
class GameListSerializer(serializers.ModelSerializer):
    team1 = TeamListSerializer()
    team2 = TeamListSerializer()
    class Meta:
        model = Game
        fields = ['id','team1','team2',
                  'time', 'tv', 'members', 'point', 
                  'win','draw','lose']

class GameDetailSerializer(serializers.ModelSerializer):
    # section = SectionSerializer()
    team1 = TeamDetailSerializer()
    team2 = TeamDetailSerializer()
    class Meta:
        model = Game
        fields = ['id','team1','team2',
                  'time', 'tv', 'members', 'point', 
                  'win','draw','lose']

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ['title','title_url','image','description']
