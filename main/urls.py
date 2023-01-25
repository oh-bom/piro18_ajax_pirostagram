from django.contrib import admin
from . import views
from django.urls import path,include

app_name='main'

urlpatterns = [
    path('',views.post_list,name='post_list'),
    path('create',views.post_create,name='post_create'),
    path('like_ajax',views.like_ajax,name='like_ajax'),
    path('comment_create',views.comment_create,name='comment_create'),
]
