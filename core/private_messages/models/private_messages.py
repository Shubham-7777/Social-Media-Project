from django.conf import settings
from django.db import models



class PrivateMesssages(models.Model):
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='sent_private_messages')
    receiver = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,  related_name='received_private_messages')
    subject = models.CharField(max_length=250)
    body = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Message - Subject - {self.subject} - Body - {self.body} -- Sent by > {self.sender} -- To -- {self.receiver}' 
     