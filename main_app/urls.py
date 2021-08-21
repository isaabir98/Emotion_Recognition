from re import template
from main_app.run import index
from django.urls import path
from main_app import views 
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('', views.index, name='index'),
    path('video_feed', views.video_feed, name='video_feed'),
    path('noob/', views.pagehome, name='noob-about'),
    path('login/', auth_view.LoginView.as_view(template_name='login.html'), name='login'),
    path('signup/',views.signup,name='signup'),
    # path('video_feed/', views.video_feed, name='video_feed'),
    path('userpanel1/',views.userpanel1,name='userpanel1'),
    path('newsapi',views.newsapi,name='newsapi'),
    ]