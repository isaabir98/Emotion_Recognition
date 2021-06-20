from main_app.run import index
from django.urls import path
from main_app import views


urlpatterns = [
    path('', views.index, name='index'),
     path('video_feed', views.video_feed, name='video_feed')
    # path('video_feed/', views.video_feed, name='video_feed'),

    ]