from django.contrib import admin
from django.urls import path
from apps.post import views
from apps.post.views import AddPost

urlpatterns = [
    path('post/<int:user_id>/', views.posts, name='posts'),
    path('postAdd/<int:user_id>/', AddPost.as_view()),
    path('<int:author_comment_id>/', views.detail, name='detail'),
    path('hello', views.hello, name='hello'),
    path('chek_username', views.chek_username, name='chek_username'),
    path('check_email', views.check_email, name='check_email'),

]
