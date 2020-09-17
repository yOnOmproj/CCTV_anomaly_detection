from django.urls import path
from . import views

app_name = "post"
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('made_by/', views.made_by, name='made_by'),
    path('video_content/', views.video_content, name='input_video'),
    path('home_number/', views.home_number, name='home_number'),
    path('error/', views.error, name='error'),
    path('insert_video/', views.insert_video, name='insert_video')
]