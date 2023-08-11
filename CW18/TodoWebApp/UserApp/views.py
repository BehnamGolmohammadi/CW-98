from django.shortcuts import render, redirect
from .forms import RegisterForm

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