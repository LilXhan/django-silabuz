from django.shortcuts import render, redirect
from django.views.generic import CreateView
from .forms import NewUserForm

class RegisterForm(CreateView):
    template_name = 'registration/register.html'
    form_class = NewUserForm
    
    def form_valid(self, form):
        form.save()

        return redirect('login')


