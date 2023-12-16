from django.contrib.auth.models import User
from django.db import models
from django.conf import settings
import os

class VerifyUser(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete = models.CASCADE)
    email = models.EmailField()
    # rank = models.CharField(max_length = 4, default = '8kyu')
    profile_picture = models.ImageField(upload_to = 'users/', blank = True)
    created = models.DateTimeField(auto_now_add = True)

    class Meta:
        verbose_name_plural = 'Verify Users'
        ordering = ['-created']
        
    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        if not self.profile_picture:
            self.profile_picture = os.path.join(settings.MEDIA_ROOT, 'default_profile_picture.png')
        super().save(*args, **kwargs)
