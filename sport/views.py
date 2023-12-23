from rest_framework.generics import RetrieveAPIView,ListAPIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView, Response
from django.http import Http404
from .models import Section, Game, News, Player
from .serializer import SectionSerializer, GameDetailSerializer, GameListSerializer, NewsSerializer, PlayerSerializer
             
class SectionListView(ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Section.objects.all()
    serializer_class = SectionSerializer

class GameListView(ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = GameListSerializer

    def get_queryset(self):
        section = self.kwargs.get('section')
        queryset = Game.objects.filter(section__slug = section)
        return queryset

class GameDetailView(RetrieveAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Game.objects.all()
    serializer_class = GameDetailSerializer

    def get_object(self):
        pk = self.kwargs.get('pk')
        section = self.kwargs.get('section')

        obj = Game.objects.filter(pk = pk,section__slug = section).first()

        if obj is None:
            raise Http404()

        return obj

class NewsView(ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = NewsSerializer

    def get_queryset(self):
        section = self.kwargs.get('section')
        queryset = News.objects.filter(section__slug = section)[:2] 
        return queryset

class PlayerDetailView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self,request, slug):
        player = Player.objects.get(slug = slug)
        player_data = PlayerSerializer(player).data
        return Response(player_data)