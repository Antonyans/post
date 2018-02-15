from django.urls import path, include
from apps.userProfile.views import UserUpdateView


urlpatterns = [
    # path('my_account', views.my_account, name='my_account'),
     path('my_account', UserUpdateView.as_view(), name='UserUpdateView')
]
