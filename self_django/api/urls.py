from . import views
from django.urls import path

urlpatterns = [
    path('hello/', views.hello),
    path('posthello/', views.posthello)
]