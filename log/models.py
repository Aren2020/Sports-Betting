from django.contrib.auth.models import User
from django.db import models

class VerifyUser(models.Model):
    user = models.OneToOneField(User,on_delete = models.CASCADE)
    email = models.EmailField()
    created = models.DateTimeField(auto_now_add = True)

    class Meta:
        verbose_name_plural = 'Verify Users'
        ordering = ['-created']
        
    def __str__(self):
        return self.user
