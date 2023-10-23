from rest_framework.generics import ListAPIView
from .models import Section
from .serializer import SectionSerializer
             
class SectionListView(ListAPIView):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer
