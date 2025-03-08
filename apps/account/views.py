from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth import logout
from django.shortcuts import redirect

class CustomLoginView(LoginView):
    template_name = 'Portal/Auth/login.html'
    success_url = reverse_lazy('portal')

def logout_view(request):
    logout(request)
    return redirect('login') 