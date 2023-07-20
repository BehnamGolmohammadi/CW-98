from django.urls import path
from . import views

app_name = 'category'

urlpatterns = [
    path('', views.all_category ,name= 'index'),
    path('categoryinfo/<int:cat_id>', views.category_detail, name='categoryinfo')
]