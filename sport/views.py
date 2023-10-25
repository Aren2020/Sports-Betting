from rest_framework.generics import ListAPIView
from .models import Section, Game
from .serializer import SectionSerializer, GameSerailizer
             
class SectionListView(ListAPIView):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer

class GameListView(ListAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerailizer