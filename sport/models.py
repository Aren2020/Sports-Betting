from django.db import models

class SportSection(models.Model):
    name = models.CharField(max_length = 150)
    slug = models.SlugField(max_length = 150)
    image = models.URLField()    

    class Meta:
        verbose_name_plural = 'Sport Sections'

    def __str__(self):
        return self.name

   