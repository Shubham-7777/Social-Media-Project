from rest_framework import serializers
from accounts.models.user import UserProfile




class UserProfileSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    
    
    class Meta:
        model = UserProfile
        fields = ["user", "email", "first_name", "last_name", "image", "date_joined"]
        #, "code"


    def get_user(self, user):
        print(user, "obj.data")
        #return obj.user.username
        obj = UserProfile.objects.get(user__username=user)
        print(UserProfileSerializer(obj, read_only=True).data)
        return UserProfileSerializer(obj, read_only=True).data

