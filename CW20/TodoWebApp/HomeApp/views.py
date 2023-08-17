from django.shortcuts import render
from TaskApp.models import Task, Category
from django.views.generic import ListView
# Create your views here.
# def home_page(request):
#     all_task = Task.objects.all()[:5]
#     all_category = Category.objects.all()[:5]
#     return render(request, 'home/home.html', {'all_task':all_task, 'all_category':all_category})

class HomePageView(ListView):
    model = Task
    template_name = 'home/home.html'
    context_object_name = 'all_task'
    queryset = Task.objects.all()[:5]

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['all_category'] = Category.objects.all()[:5]
        return context