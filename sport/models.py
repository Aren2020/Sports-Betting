from django.db import models
from datetime import datetime

class Section(models.Model):
    name = models.CharField(max_length = 150)
    slug = models.SlugField(max_length = 150)
    image = models.URLField()    

    def __str__(self):
        return self.name

class Team(models.Model):
    name = models.CharField(max_length = 150)
    slug = models.SlugField(max_length = 150)
    image = models.URLField()

    def __str__(self):
        return self.name

class Player(models.Model):
    name = models.CharField(max_length = 150)
    slug = models.CharField(max_length = 150)
    image = models.URLField()
    team = models.ForeignKey(Team,related_name = 'players',on_delete = models.CASCADE)

    def __str__(self):
        return self.name

class Game(models.Model):
    section = models.ForeignKey(Section, on_delete = models.CASCADE)
    team1 = models.ForeignKey(Team,related_name = 'games1' ,on_delete = models.CASCADE)    
    team2 = models.ForeignKey(Team,related_name = 'games2' ,on_delete = models.CASCADE)

    time = models.DateTimeField(default= datetime(2023,12,8,12,56,00))
    tv = models.BooleanField(default = False)
    members = models.IntegerField(default = 0)
    point = models.IntegerField(default = 100)

    win = models.DecimalField(max_digits=10, decimal_places=2, default = 1.0)
    draw = models.DecimalField(max_digits=10, decimal_places=2, default = 1.0)
    lose = models.DecimalField(max_digits=10, decimal_places=2, default = 1.0)    
    
    def __str__(self):
        return f'{self.team1} vs {self.team2}'

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
