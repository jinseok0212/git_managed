from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . serializers import UserRegisterSerializer
from rest_framework.permissions import IsAuthenticated
from .serializers import UserInfoSerializer

#회원가입 결과 보여주려고 

class UserRegisterAPIView(APIView):

    def post(self, request):
        serializer = UserRegisterSerializer(data = request.data)
        
        if serializer.is_valid():
            
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class UserInfoAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserInfoSerializer(request.user)
        return Response(serializer.data)