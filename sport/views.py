from rest_framework.generics import RetrieveAPIView,ListAPIView
from django.http import Http404
from .models import Section, Game, News
from .serializer import SectionSerializer, GameDetailSerializer, GameListSerializer, NewsSerializer
             
class SectionListView(ListAPIView):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer

class GameListView(ListAPIView):
    serializer_class = GameListSerializer

    def get_queryset(self):
        section = self.kwargs.get('section')
        queryset = Game.objects.filter(section__slug = section)
        return queryset

class GameDetailView(RetrieveAPIView):
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
    serializer_class = NewsSerializer

    def get_queryset(self):
        section = self.kwargs.get('section')
        queryset = News.objects.filter(section__slug = section)[:2] 
        return queryset