from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

app_name = 'user'

urlpatterns = [
    path('create/', views.create_user, name='create'),
    path('login/', views.LoginUser.as_view(), name='login'),
    path('logout/', views.LogoutUser.as_view(), name='logout'),
]