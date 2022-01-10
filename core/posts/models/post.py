from django.conf import settings
from django.db import models


class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    body = models.TextField()
    image = models.ImageField(upload_to='posts',blank=True, null=True)
    
    
    def __str__(self):
        return f'title = {self.title}, id = {self.id}, username = {self.user.username}' 
    
    