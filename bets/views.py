from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
import datetime
from sport.models import Game
from .models import Bets

class BetCreateView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        game_id = request.POST.get('game_id')
        amount = request.POST.get('amount')
        user_choice = request.POST.get('user_choice')
        user = request.user
        game = Game.objects.get(id = int(game_id))

        if not Bets.objects.filter(game = game,
                                   user = request.user,
                                   created__lt = datetime.datetime.now() - datetime.timedelta(minutes=1, seconds=30)).exists():
            if user.verifyuser.balance < int(amount):
                return Response({'msg': 'Not enough funds'})
            user.verifyuser.balance -= int(amount)
            user.verifyuser.save()
            
            Bets.objects.create(
                            user = request.user,
                            game = game,
                            amount = amount,
                            user_choice = user_choice)
        else:
            return Response({'msg': 'Try 2 minutes later'})
        
        return Response({'status': 'ok'})

class BetListView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        user_choice = {
            'w': 'win',
            'l': 'lose',
            'd': 'draw'
        }
        queryset = Bets.objects.filter(user = user)

        response = [
            {
                'amount': bet.amount,
                'team1': {
                    'name': bet.game.team1.name,
                    'image': self.url_creator(request, bet.game.team1.image),
                },
                'team2':{ 
                    'name': bet.game.team2.name,
                    'image': self.url_creator(request, bet.game.team2.image),
                },
                'kf': getattr(bet.game, user_choice[bet.user_choice]),
            } for bet in queryset
        ]
        return Response(response)
    
    def url_creator(self, request, image):
        base_url = request.build_absolute_uri('/')[:-1]
        image_url = base_url + '/media' + image.url.rsplit('media')[-1]
        return image_url

class BetWinnerView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        user_choice = {
            'w': 'win',
            'l': 'lose',
            'd': 'draw'
        }

        for bet in Bets.objects.filter(user = user).exclude(win_choice = ''):
            if bet.check_win():
                amount =  bet.amount
                kf =  getattr(bet.game, user_choice[bet.user_choice]) 
                user.verifyuser.balance += amount * kf
        Bets.objects.filter(user = user).exclude(win_choice = '').delete()
        user.verifyuser.save()
        return Response({'status': 'ok'})
