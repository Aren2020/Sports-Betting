from rest_framework.generics import ListAPIView
from .models import SportSection
from .serializer import SportSectionSerializer
             
class SportSectionListView(ListAPIView):
    queryset = SportSection.objects.all()
    serializer_class = SportSectionSerializer
