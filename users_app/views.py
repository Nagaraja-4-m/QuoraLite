from django.views import View
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth import  login
from django.shortcuts import redirect
from users_app.models import UserAccount
from auth_app.mixins import BaseAuthenticatedView
from core_app.models import Questions, Answers

class UsersView(View):
    template_name = 'register.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        data=request.POST.dict()
        if UserAccount.objects.filter(email=data['email']).exists():
            context = {'error_message': "User with this email ID already exists"}
            return render(request, self.template_name, context=context)
        else:
            password=data.pop('password')
            user=UserAccount.objects.create(**data)
            user.set_password(password)
            user.save()
            login(request, user)
            return redirect('/')

class UsersDataView(BaseAuthenticatedView,View):
    answered_template_name = 'my_answered.html'
    questioned_template_name = 'my_questioned.html'

    def get(self, request, *args, **kwargs):
        Type = kwargs['type']
        if Type == 'qs':
            data={'questions':Questions.objects.filter(asked_by = request.user).all()}
            return render(request, self.questioned_template_name, context=data)
        else:
            data={'answers':Answers.objects.filter(answer_by = request.user).all()}
            return render(request, self.answered_template_name, context=data)