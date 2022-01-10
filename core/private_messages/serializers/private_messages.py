from rest_framework import serializers
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from private_messages.models.private_messages import PrivateMesssages
from accounts.serializers.user import UserProfileSerializer
User = get_user_model()



class PrivateMessagesSerializer(serializers.ModelSerializer):
    #sender = UserProfileSerializer()
    #receiver = UserProfileSerializer()
    
    
    class Meta:
        model = PrivateMesssages
        fields = ['sender', 'receiver', 'subject', 'body', 'created_date', 'modified_date']
        
        
        
        
class PrivateMessagesCreateSerializer(serializers.ModelSerializer):
    #sender = UserProfileSerializer()
    sender = serializers.CharField(default=serializers.CurrentUserDefault())

    
    class Meta:
        model = PrivateMesssages
        fields = ['sender', 'receiver', 'subject', 'body', 'created_date', 'modified_date']