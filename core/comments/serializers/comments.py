from rest_framework import serializers
from comments.models.comments import Comments

from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
User = get_user_model()



class CommentSerializer(serializers.ModelSerializer):
    
    user = serializers.CharField(default=serializers.CurrentUserDefault())
    
    
    class Meta:
        model = Comments
        fields = ['user', 'post', 'comment', 'created_date', 'modified_date']
           
        
        
        
"""
    def validate_user(self, user):

        if user != self.context['request'].user:
            raise serializers.ValidationError('You can not create post replies for other users')
        return user


    def validate(self, data):

        if self.instance.user != self.context['request'].user:
            raise serializers.ValidationError('You can not edit post replies from other users')
        return data

"""