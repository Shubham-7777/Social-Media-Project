from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView




from accounts.serializers.user import UserProfileSerializer
from accounts.models.user import UserProfile 


class UserView(APIView):
    

    def get(self, request):
        """
        List users
        """

        users = UserProfile.objects.filter(user=self.kwargs.get('user'))
        return Response(UserProfileSerializer(users, many=True).data)


