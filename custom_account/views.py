from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.conf import settings
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from .form import CustomUserForm

User = get_user_model()        

def register(request):
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            user = form.save() 
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('home')
    else:
        form = CustomUserForm()
    
    return render(request, 'account/register.html', {'form': form})

class CustomLoginView(LoginView):
    template_name = 'account/signin.html'

    def form_valid(self, form):
        user = form.get_user()
        login(self.request, user, backend='django.contrib.auth.backends.ModelBackend')
        redirect_to = self.request.GET.get('next', 'home')
        return redirect(redirect_to)


class AdminLoginView(LoginView):
    template_name = 'admin/login.html'
    success_url = reverse_lazy('admin:home')

class AdminLogoutView(LogoutView):
    next_page = reverse_lazy('admin-login')