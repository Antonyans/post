from django.urls import path, include
from apps.register import views
from django.contrib.auth.views import logout
from django.conf import settings


urlpatterns = [
    path('signup', views.signup, name='signup'),
    path('login', views.signin, name='signin'),
    path('logout', logout, {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout')


]
