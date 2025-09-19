from . import views
from django.urls import path

urlpatterns = [
    path('',views.tweet_list, name='tweet-list'),
    path('tweet-create/', views.tweet_create, name='tweet-create'),
    path('tweet-edit/<int:tweet_id>/', views.tweet_edit, name='tweet-edit'),
    path('tweet-delete/<int:tweet_id>/', views.delete_tweet, name='tweet-delete'),
    
]