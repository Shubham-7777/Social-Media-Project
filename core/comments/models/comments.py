from django.db import models
from django.conf import settings
from posts.models.post import Post


class Comments(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return f'user = {self.user}, post = {self.post}, comment = {self.comment}, id = {self.id}'