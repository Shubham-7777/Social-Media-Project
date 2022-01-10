"""
from django.conf import settings
from django.db import models

User = settings.AUTH_USER_MODEL
#from django.contrib.auth.models import User


class Profile(models.Model):
    image = models.ImageField(upload_to='profile-pictures', blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    
    def __str_(self):
        return self.user.email
    
    
"""