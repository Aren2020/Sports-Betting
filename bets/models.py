from django.db import models
from django.conf import settings
from sport.models import Game
import datetime

class Bets(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                                on_delete = models.CASCADE)
    game = models.ForeignKey(Game,
                             related_name = 'bets',
                             on_delete = models.CASCADE)
    amount = models.PositiveIntegerField(default = 0)
    user_choice = models.CharField(max_length = 1)
    win_choice = models.CharField(max_length = 1, blank = True)
    created = models.DateTimeField(auto_now_add = True) # default = datetime.datetime.now())

    def check_win(self):
        return self.user_choice == self.win_choice       
    
    def __str__(self):
        return f'{self.user.username}`s bet for game [ {str(self.game)} ]'

    class Meta:
        verbose_name_plural = 'Bets'