from .views import UserRegisterAPIView
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('signup/', UserRegisterAPIView.as_view()), # 연결 
    path('login/', TokenObtainPairView.as_view()),
]