from django.urls import path
from . import views


urlpatterns = [
    path('upload/', views.upload_file, name='upload_file'),
    path('download/<int:file_id>/', views.download_file, name='download_file'),
    path('', views.user_registration, name='user_registration'),
    path('login/', views.user_login, name='user_login'),
      
]


