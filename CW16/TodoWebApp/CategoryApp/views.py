from django.shortcuts import render
from TaskApp.models import Task, Category


# Create your views here.
def all_category(request):
    all_category = Category.objects.all()
    return render(request, 'category/category.html', context= {'all_category': all_category})

def category_detail(request, cat_id):
    category = Category.objects.get(id=cat_id)
    return render(request, 'category/category.html', {'single_category': category})