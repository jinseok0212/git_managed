from .views import UserRegisterAPIView, UserInfoAPIView # 유저정보 조회 해야겠지. 
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('signup/', UserRegisterAPIView.as_view()), # 연결 
    path('login/', TokenObtainPairView.as_view()),
    path('user/', UserInfoAPIView.as_view()), # 유저정보 조회 해야겠제.
]

