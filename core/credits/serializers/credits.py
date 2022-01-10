from rest_framework import serializers
from credits.models.credits import Invitation, Transfer, User, Wallet
from accounts.serializers.user import UserProfileSerializer


class InvitationSerializer(serializers.ModelSerializer):
    #sender = UserProfileSerializer()
    #receiver = UserProfileSerializer()
    
    
    class Meta:
        model = Invitation
        fields = ["code", "sender", "receiver", "created_date", "modified_date"]
        


class InvitationSerializerCreate(serializers.ModelSerializer):
    #sender = UserProfileSerializer()
    #receiver = serializers.SerializerMethodField()
    #receiver = UserProfileSerializer()
    #sender = serializers.HiddenField(default=serializers.CurrentUserDefault())
    sender = serializers.CharField(default=serializers.CurrentUserDefault())

    
    class Meta:
        model = Invitation
        fields = ["code", "sender", "receiver", "created_date", "modified_date"]

"""
    def get_receiver(self, obj):
        print(obj, "obj.data")
        return obj.receiver

"""

class TransferSerializer(serializers.ModelSerializer):
    #sender = UserProfileSerializer()
    #receiver = UserProfileSerializer()
    
    
    class Meta:
        model = Transfer
        fields = ["sender", "receiver", "amount", "created_date", "modified_date"]
      

class TransferSerializerCreate(serializers.ModelSerializer):
    #receiver = UserProfileSerializer()
    #receiver = serializers.SerializerMethodField()
    #sender = serializers.HiddenField(default=serializers.CurrentUserDefault())
    #receiver = serializers.SlugRelatedField(read_only=True, slug_field='receiver.user')
    sender = serializers.CharField(default=serializers.CurrentUserDefault())
    
    
    class Meta:
        model = Transfer
        fields = ["sender", "receiver", "amount", "created_date", "modified_date"]


    def validate(self, data):
        '''
        Already excuted this functionality in TransferView (views.py) THIS IS JUST FOR EXAMPLE - can also validate in serializer
        '''

        print(data)
        sender = data.get("sender"),
        receiver = data.get("receiver")

        sender_wallet, _ = Wallet.objects.get_or_create(user=data.get('sender'))
        receiver_wallet, _= Wallet.objects.get_or_create(user=data.get('receiver'))
        print(sender_wallet ,type(sender_wallet),  'sender_wallet')
        print(sender_wallet.balance ,type(sender_wallet.balance),  'sender_wallet.balance')
        print(receiver_wallet)
        if data.get('amount') <= 0:
            raise serializers.ValidationError('Amount must be greater than zero')
        if data.get('amount') > sender_wallet.balance:
            raise serializers.ValidationError('Not Enough credit on sender wallet')
        return data



"""
    def get_receiver(self, obj):
        return obj.receiver.user
"""


class WalletSerializer(serializers.ModelSerializer):
    #user = UserProfileSerializer()
    
    
    class Meta:
        model = Wallet
        fields = ["user", "balance"]