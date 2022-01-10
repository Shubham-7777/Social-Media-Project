import uuid
from django.conf import settings
from django.db import models


User = settings.AUTH_USER_MODEL

class Invitation(models.Model):
    code = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sender_invitations")
    receiver = models.ForeignKey(User,  null=True, blank=True, default=None,on_delete=models.CASCADE, related_name="receiver_invitations")
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    
    
    class Meta:
        default_related_name = "invitations"
        
    def __str__(self):
        return f'sender - {self.sender} - receiver - {self.receiver} - code - {self.code}'    

    
    
class Transfer(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender_transfers')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver_transfers')
    amount = models.IntegerField()
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        default_related_name = 'transfers'

    def __str__(self):
        return f'sender > {self.sender} > receiver > {self.receiver} > {self.amount}'



class Wallet(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.user} = {self.balance}' 

