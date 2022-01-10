from rest_framework import serializers
from posts.models.post import Post
from accounts.serializers.user import UserProfileSerializer
from accounts.models.user import UserProfile
from django.shortcuts import get_object_or_404
from accounts.models.user import UserProfile 
from django.contrib.auth import get_user_model
User = get_user_model()

class PostSerializer(serializers.ModelSerializer):
    #user = UserProfileSerializer()
    #user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    user = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ["user", "title", "body", "image"]
        
        
    def get_user(self, obj):
        print(obj, "obj.data")
        return obj.user.username

    def validate(self, data):
        print(self.instance.user, 'validate')  
        print(self.context['request'].user, 'validate')
        if self.instance.user != self.context['request'].user:
            raise serializers.ValidationError('You can not edit post replies from other users')
        return data
    

class PostSerializerCreate(serializers.ModelSerializer):
    #user = serializers.PrimaryKeyRelatedField(default=serializers.CurrentUserDefault(), queryset=UserProfile.objects.all())
    user = serializers.CharField(default=serializers.CurrentUserDefault())
    #user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    #owner = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Post
        fields = ["user", "title", "body", "image"]
        
        
        
        
        

    
