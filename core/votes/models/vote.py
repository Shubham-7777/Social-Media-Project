from django.conf import settings
from django.db import models
from posts.models.post import Post


#VOTE_UP = 1
#VOTE_DOWN = -1

VOTE_VALUE_CHOICES = (
    (1, 'Up'),
    (-1, 'Down')
)

class Vote(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    value = models.IntegerField(choices=VOTE_VALUE_CHOICES)
    

    
    def __str__(self):
        return f' post: {self.post.title},  user:  {self.user.username}, value: {self.value}'