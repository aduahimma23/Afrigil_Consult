from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LoginView
from .form import CustomUserForm
from django.urls import reverse_lazy
from django.views import View

def register(request):
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('account:login')
    else:
        form = CustomUserForm()
    
    return render(request, 'account/register.html', {'form': form})

class CustomLoginView(LoginView):
    template_name = 'account/signin.html'

    def form_valid(self, form):
        login(self.request, form.get_user())
        return redirect('home')
