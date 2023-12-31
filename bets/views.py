from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
import datetime
from django.db import models
from sport.models import Game
from .models import Bets
from .serializer import BetListSerializer

class BetCreateView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        game_id = request.POST.get('game_id')
        amount = request.POST.get('amount')
        user_choice = request.POST.get('user_choice')

        game = Game.objects.get(id = int(game_id))
        if not Bets.objects.filter(game = game,
                                   user = request.user,
                                   created__lt = datetime.datetime.now() - datetime.timedelta(minutes=1, seconds=30)).exists():
            Bets.objects.create(
                            user = request.user,
                            game = game,
                            amount = amount,
                            user_choice = user_choice)
        else:
            return Response({'msg': 'Try 2 minute later'})
        
        return Response({'status': 'Ok'})

class BetListView(ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = BetListSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = Bets.objects.filter(user = user)
        return queryset