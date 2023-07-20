from django.shortcuts import render
from TaskApp.models import Task

# Create your views here.
def home_page(request):
    all_task = Task.objects.all().values()[:5]
    return render(request, 'home/home.html', {'all_task':all_task})