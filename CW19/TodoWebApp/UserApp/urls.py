from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('create/', views.create_user, name='create'),
    # path('login/', views.login_user, name='login'),
]