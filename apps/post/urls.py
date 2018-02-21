from django.contrib import admin
from django.urls import path
from apps.post import views
from apps.post.views import AddPost

urlpatterns = [
    path('post/', views.posts, name='posts'),
    path('post/get/<int:post_id>/', views.comments, name='comments'),

    path('postAdd/<int:user_id>/', AddPost.as_view()),
    path('hello', views.hello, name='hello'),
    path('chek_username', views.chek_username, name='chek_username'),
    path('check_email', views.check_email, name='check_email'),
    path('post/search/', views.search, name='search'),
    path('post/addlike/<int:post_id>/', views.addlike, name='addlike'),



]
