from typing import Any, Dict
from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.contrib import messages

# Create your views here.
def create_user(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        print (form.data)
        if form.is_valid():
            form.save()
            
            return redirect('/')

    else:
        form = RegisterForm()
        
    context = {
        'create_form': form 
    }

    return render(request= request, template_name= 'user/user.html', context= context)

class login_user(LoginView):
    redirect_authenticated_user = True
    template_name = 'user/user.html'

    def get_success_url(self):
        return reverse_lazy('home:index') 
        
    def form_invalid(self, form):
        messages.error(self.request,'Invalid username or password')
        return self.render_to_response(self.get_context_data(form=form))
    
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['login_form'] = True
        return context