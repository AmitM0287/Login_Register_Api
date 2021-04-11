from django.urls import path
from . import views


urlpatterns = [
    path('login/user/', views.user_login, name='user_login'),
]
