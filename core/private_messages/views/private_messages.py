from django.db.models import Q
from django.shortcuts import get_list_or_404
from django.shortcuts import get_object_or_404
from private_messages.models.private_messages import PrivateMesssages
from private_messages.serializers.private_messages import PrivateMessagesSerializer, PrivateMessagesCreateSerializer


from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView



class PrivateMessagesView(APIView):
    
    
    def get(self, request):
        user = request.user
        obj = PrivateMesssages.objects.filter(
            Q(receiver= user) | 
            Q(sender = user)
        )
        serializer = PrivateMessagesSerializer(obj, many=True)
        return Response({"DATA" : serializer.data}, status=status.HTTP_201_CREATED)
    


    def post(self, request):
        serializer = PrivateMessagesCreateSerializer(data=request.data, context = {'request' : request})
        if serializer.is_valid():
            serializer.save()
            return Response({"DATA" : serializer.data}, status=status.HTTP_201_CREATED)    
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    
    
    
    
class PrivateMesssagesDetailView(APIView):
    
    
    def get(self, request, id):
        print(id)
        user = request.user
        obj = PrivateMesssages.objects.filter(
            Q(receiver = user) |
            Q(sender = user),
            pk = id
        ).first()
        if not obj:
            print("message doesn't exist")
            return Response({"MESSAGE", "Private Message Doesnt Exist"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer = PrivateMessagesSerializer(obj)
            return Response({'DATA' : serializer.data}, status=status.HTTP_201_CREATED)
        