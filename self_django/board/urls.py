from django.urls import path
from . import views

urlpatterns = [

    path(' ', views.Post_list, name= 'post_list'),
    path('new/', views.Post_create, name= 'post_create'),
    path('<int:pk>', views.Post_detail, name= 'post_detail'),
    path('<int:pk>/edit/', views.Post_edit, name= 'post_edit'),
    path('<int:pk>/delete/', views.post_delete, name= 'post_delete'),
]

