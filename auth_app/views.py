from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.views import View
from django.shortcuts import redirect
from auth_app.mixins import BaseAuthenticatedView

# Create your views here.
class LoginView(View):
    template_name = 'login.html'
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        data=request.POST.dict()
        user = authenticate(request, email=data['email'], password=data['password'])
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return render(request, self.template_name, {'error_message': 'Invalid credentials'})
        
class LogoutView(BaseAuthenticatedView,View):
    template_name = 'index.html'
    
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('/')
        return render(request, self.template_name)