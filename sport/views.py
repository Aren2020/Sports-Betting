from rest_framework.generics import RetrieveAPIView,ListAPIView
from django.http import Http404
from .models import Section, Game
from .serializer import SectionSerializer, GameDetailSerailizer, GameListSerailizer
             
class SectionListView(ListAPIView):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer

class GameListView(ListAPIView):
    serializer_class = GameListSerailizer

    def get_queryset(self):
        section = self.kwargs.get('section')
        queryset = Game.objects.filter(section__slug = section)
        return queryset

class GameDetailView(RetrieveAPIView):
    queryset = Game.objects.all()
    serializer_class = GameDetailSerailizer

    def get_object(self):
        pk = self.kwargs.get('pk')
        section = self.kwargs.get('section')

        obj = Game.objects.filter(pk = pk,section__slug = section).first()

        if obj is None:
            raise Http404()

        return obj
