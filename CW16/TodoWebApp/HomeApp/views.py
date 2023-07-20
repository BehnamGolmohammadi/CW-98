from django.shortcuts import render
from TaskApp.models import Task, Category

# Create your views here.
def home_page(request):
    all_task = Task.objects.all()[:5]
    all_category = Category.objects.all()[:5]
    return render(request, 'home/home.html', {'all_task':all_task, 'all_category':all_category})