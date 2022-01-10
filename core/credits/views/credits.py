import json

from django.http.response import HttpResponse
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from credits.models.credits import Invitation, Transfer, Wallet 
from credits.serializers.credits import InvitationSerializer, InvitationSerializerCreate, \
                                        TransferSerializer, TransferSerializerCreate, WalletSerializer



class InvitationsView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    # Remaining
    # invitation_filter
    # filter_query_params
    
    
    def get(self, request):
        obj = Invitation.objects.all()
        serializers = InvitationSerializer(obj, many=True)
        data = serializers.data
        return Response({"DATA" : data}, status=status.HTTP_201_CREATED)
    

    def post(self, request):
        serializer = InvitationSerializerCreate(data=request.data, context={"request": request})
        if serializer.is_valid():
            serializer.save()
            data=serializer.data
            return Response({"DATA" : data}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class TransferView(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    
    
    def get(self, request):
        obj = Transfer.objects.all()
        serializers = TransferSerializer(obj, many=True)
        data = serializers.data
        return Response({"DATA" : data}, status=status.HTTP_201_CREATED)
    
    
    
    
    def post(self, request):
        sender = self.request.user
        amount = self.request.data.get('amount')
        receiver = self.request.data.get('receiver')
        
        sender_obj, created = Wallet.objects.get_or_create(user__username=sender)
        receiver_obj, created = Wallet.objects.get_or_create(user_id=receiver)
        
        if sender_obj.balance <= 0: 
            return Response("Amount must be greater than zero", status=status.HTTP_400_BAD_REQUEST)
        
        elif sender_obj.balance < int(amount): 
            return Response("Insuffient Sender Wallet Balance", status=status.HTTP_400_BAD_REQUEST)
        
        
        else:
            sender_obj.balance -= int(amount)
            receiver_obj.balance += int(amount)
            sender_obj.save()
            receiver_obj.save()

            serializer = TransferSerializerCreate(data=request.data, context={"request" : request})
            if serializer.is_valid():
                serializer.save()
                data = serializer.data
                return Response({"DATA" : data}, status=status.HTTP_201_CREATED)
            else:
                return Response({"ERRORS" : serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class WalletView(APIView):
    
    def get(self, request, id):
        print(id, 'id')
        wallet_obj = Wallet.objects.filter(user__id=id)
        if wallet_obj.exists():
            serializer = WalletSerializer(wallet_obj, many=True)
            return Response({"WALLET INFO" : serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({"ERRORS" : "USER WALLET DOESNT EXIST"})
       