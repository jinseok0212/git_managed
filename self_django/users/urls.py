from .views import UserRegisterAPIView
from django.urls import path

urlpatterns = [
    path('signup/', UserRegisterAPIView.as_view()), # 연결 
]