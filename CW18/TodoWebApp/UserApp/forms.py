from django import forms
from django.contrib.auth.forms import UserCreationForm
from UserApp.models import User

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "password1",
            "password2",
        ]

        def __init__(self, *args, **kwargs) -> None:
            super(RegisterForm, self).__init__(*args, **kwargs)

            self.fields['username'].widget.attrs['name'] = 'username'
            self.fields['email'].widget.attrs['name'] = 'email'
            self.fields['password1'].widget.attrs['name'] = 'password1'
            self.fields['password2'].widget.attrs['name'] = 'password2'

        def clean_mail(self): 
            data = self.cleaned_data['email']
            if User.objects.filter(mail=data).exists():
                raise forms.ValidationError("This email is already exists")