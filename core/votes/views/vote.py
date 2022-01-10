from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from votes.models.vote import Vote
from posts.models.post import Post
from votes.serializers.vote import  PostVoteSerializer,  PostVoteSerializerCreate, PostVoteSerializerUpdate
from posts.serializers.post import PostSerializer

class PostVoteView(APIView):
    
    
    def get(self, request):
        user = self.request.user
        #obj = Post.objects.filter(user__username=user)
        #serializer = PostSerializer(obj, many=True)
        obj = Vote.objects.filter(user__username=user)
        serializer = PostVoteSerializer(obj, many=True)
        return Response({"message" : "GET request Success", "serializer" : serializer.data}, status=status.HTTP_201_CREATED)
    
    
    
    
    def post(self, request):
        #print(self.user, "self.instance.user") 
        user = self.request.user
        post = self.request.data['post']
        value = self.request.data['value']
        obj = Vote.objects.filter(user__username=user, post=post, value=value)
        if obj.exists():
            print("exists")
            return Response({"message" : "You already voted"})
        else:
            print("NOT exists")
            serializer = PostVoteSerializerCreate(data=request.data, context={'request': request})
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                data = serializer.data
                return Response({"message" : "POST request Success", "serializer" : data}, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
            


class PostUpdateView(APIView):
    
    
    def patch(self, request, post_vote_id):
        user = self.request.user
        obj = Vote.objects.filter(user=user, post=post_vote_id).first()
        if obj is not None:
            serializer = PostVoteSerializerUpdate(obj, data=request.data, context={'request': request})
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response({"message" : "PATCH request Success", "serializer" : serializer.data}, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"message" : "Object | Vote does NOT exists, plz create from post first"}, status=status.HTTP_400_BAD_REQUEST)
            
            
            
    """
        user = self.request.user
        post_vote_id = post_vote_id
        value = self.request.data['value']
        print(user,"post_vote_id", post_vote_id, "value", value)
        obj = Vote.objects.filter(user__username=user, post=post_vote_id, value=value)
        """
    
    def delete(self, request, post_vote_id):
        user = self.request.user
        obj = Vote.objects.filter(user=user, post=post_vote_id)
        print(obj)
        if obj.exists():
            obj.delete()
            return Response({"message" : "DELETE request Success"})
        else:
            return Response({"message" : "OBJECT already DELETED OR DOESNOT EXISTS"})
                
    
    
    