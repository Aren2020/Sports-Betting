from django.db import models
from datetime import datetime
import os,random

class Section(models.Model):
    name = models.CharField(max_length = 150)
    slug = models.SlugField(max_length = 150)
    image = models.URLField()    

    def __str__(self):
        return self.name

def team_upload_to_name(instance,filename):
    return os.path.join(instance.name, filename)

class Team(models.Model):
    name = models.CharField(max_length = 150)
    slug = models.SlugField(max_length = 150)
    image = models.ImageField(upload_to = team_upload_to_name,blank=True)

    def __str__(self):
        return self.name

def player_upload_to_name(instance, filename):
    return os.path.join(instance.team.name, instance.name, filename)

class Player(models.Model):
    name = models.CharField(max_length = 150)
    slug = models.CharField(max_length = 150)
    image = models.ImageField(upload_to = player_upload_to_name)
    team = models.ForeignKey(Team,related_name = 'players',on_delete = models.CASCADE)
    position = models.CharField(max_length = 12,default = 'replacement')

    def __str__(self):
        return self.name

class Game(models.Model):
    section = models.ForeignKey(Section, on_delete = models.CASCADE)
    team1 = models.ForeignKey(Team,related_name = 'games1' ,on_delete = models.CASCADE)    
    team2 = models.ForeignKey(Team,related_name = 'games2' ,on_delete = models.CASCADE)

    time = models.DateTimeField(default= datetime(2023,12,8,12,56,00))
    tv = models.BooleanField(default = False)
    members = models.IntegerField(default = 0)
    point = models.IntegerField(blank = True)

    win = models.DecimalField(max_digits=10, decimal_places=2, default = 1.0)
    draw = models.DecimalField(max_digits=10, decimal_places=2, default = 1.0)
    lose = models.DecimalField(max_digits=10, decimal_places=2, default = 1.0)    
    
    def __str__(self):
        return f'{self.team1} vs {self.team2}'
    
    def save(self, *args, **kwargs):
        if not self.point:
            self.point = random.randint(100,1000)
        return super().save(*args, **kwargs)

class News(models.Model):
    title = models.CharField(max_length=1000)
    title_url = models.URLField()
    image = models.ImageField(upload_to = 'image/')
    description = models.TextField()
    section = models.ForeignKey(Section, related_name = 'news', on_delete = models.CASCADE)
    created = models.DateTimeField(auto_now_add = True)

    class Meta:
        verbose_name_plural = 'News'
        ordering = ['-created']

    def __str__(self):
        return self.title
