from django.shortcuts import get_list_or_404
from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from posts.models.post import Post
from posts.serializers.post import PostSerializer, PostSerializerCreate




class PostView(APIView):
    
    def get(self, request):
        post = Post.objects.all()
        serializer = PostSerializer(post, many=True)
        return Response({"message" : "SUCCESS", "serializer" : serializer.data})



class PostUserView(APIView):
    
    
    def get(self, request, user):
        post = Post.objects.filter(user__username=user)
        serializer = PostSerializer(post, many=True)
        return Response({"message" : "SUCCESS", "USER" : self.kwargs.get("user"), "serializer" : serializer.data})


    def post(self, request, user):
        print(request.data, "request.data")
        print(self.request.user, "self.request.user")
        serializer = PostSerializerCreate(data=request.data, context = {"request" : request})
        if serializer.is_valid():
            serializer.save()
            data = serializer.data
            return Response({"DATA" : data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    


class PostDetailView(APIView):
    
    def get(self, request, post_id):         
        obj = get_object_or_404(Post, id=post_id)
        serializer = PostSerializer(obj)
        return Response({"message" : "SUCCESS", "serializer" : serializer.data})
            
    
    def put(self, request,  post_id):
        #obj = get_object_or_404(Post, id=post_id)
        obj = Post.objects.filter(pk=post_id, user__username=request.user).first()
    
        if obj is None:
            return Response({"MESSAGE" : "Post doesnot exist or Belongs to different user so cannot be edited by you"}, status=status.HTTP_400_BAD_REQUEST)
            
        serializer = PostSerializer(obj, data=request.data, context = {"request" : request})
        if serializer.is_valid():
            serializer.save()
            return Response({"message" : "SUCCESS", "serializer" : serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    
    def delete(self, request, post_id):
        obj = get_object_or_404(Post, pk=post_id)
        if obj.user != request.user:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

        
"""
"""
"""
    
    def patch(self, request, post_id):
        obj = get_object_or_404(Post, pk=post_id)
        serializer = PostSerializer(obj, data=request.data, context = {"request" : request}, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message" : "SUCCESS", "serializer" : serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        """