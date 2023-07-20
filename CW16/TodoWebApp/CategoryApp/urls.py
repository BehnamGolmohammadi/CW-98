from django.urls import path
from . import views

app_name = 'category'

urlpatterns = [
    path('', views.all_category ,name= 'index'),
    # path('category/<int:task_id>', views.task_detail, name='categoryinfo')
]