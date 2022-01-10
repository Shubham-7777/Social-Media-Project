from django.shortcuts import get_list_or_404
from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from comments.models.comments import Comments
from comments.serializers.comments import CommentSerializer



class CommentsView(APIView):
    
    def post(self, request):
        serializer = CommentSerializer(data=request.data, context = {'request' : request})
        if serializer.is_valid():
            serializer.save()
            return Response({"message" : "GET request Success", "serializer" : serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({"ERRORS" : serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
                


class CommentsUpdateView(APIView):


    def patch(self, request, id):
        obj = Comments.objects.filter(id=id, user=request.user).first()
        if obj is not None:
            serializer = CommentSerializer(obj, data=request.data, context={'request': request}, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"message" : "PATCH request Success", "serializer" : serializer.data}, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"Message" : "Commented Post doesnt exist or Comment is of different User"}, status=status.HTTP_400_BAD_REQUEST)



    def delete(self, request, id):        
        obj = get_object_or_404(Comments, id=id)
        print(obj.user)
        if obj.user != request.user:
            return Response({"message" : "UNAUTHORIZED"}, status=status.HTTP_401_UNAUTHORIZED)
        obj.delete()
        return Response({"message" : "DELETE request Success"}, status=status.HTTP_204_NO_CONTENT)
    

