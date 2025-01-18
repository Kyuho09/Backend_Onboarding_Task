from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import SignupSerializer

class SignupView(APIView):
    def post(self, request):
        # 요청 데이터를 Serializer에 전달
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            # 유저 생성
            user = serializer.save()
            # 성공 응답
            return Response({
                "username": user.username,
                "nickname": user.nickname,
                "roles": [{"role": "USER"}]
            }, status=status.HTTP_201_CREATED)
        # 유효하지 않은 데이터 응답
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
