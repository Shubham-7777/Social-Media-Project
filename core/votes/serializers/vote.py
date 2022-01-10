from rest_framework import serializers
from votes.models.vote import Vote


class PostVoteSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Vote
        fields = ["user", "post", "value"]
        

class PostVoteSerializerCreate(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Vote
        fields = ["user", "post", "value"]


class PostVoteSerializerUpdate(serializers.ModelSerializer):
    #user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Vote
        #fields = ["user", "value"]
        exclude = ("post", "user", )

