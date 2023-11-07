from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse
from auth_app.mixins import BaseAuthenticatedView
from django.views import View
from core_app.models import *

# Create your views here.
class IndexView(View):
    template_name = 'index.html'
    
    def get(self, request, *args, **kwargs):
        context={'questions':Questions.objects.all().order_by('-id')}
        return render(request, self.template_name, context)
    

class AskQuestionView(BaseAuthenticatedView,View):
    template_name = 'index.html'

    def post(self, request, *args, **kwargs):
        try:
            data=request.POST.dict()
            Questions.objects.create(**data, asked_by = request.user)
            return redirect('/')
        except:
            return redirect('/')
            return render(request, self.template_name)    
    
class SingleQuestion(View):
    template_name = 'question.html'

    def get(self, request, *args, **kwargs):
        try:
            context={'question':Questions.objects.filter(question_slug=kwargs['question_slug']).get()}
            return render(request, self.template_name, context)
        except Questions.DoesNotExist:
            return redirect('/')
   

class SingleQuestionAnserView(BaseAuthenticatedView,View):
    template_name = 'question.html'

    def get(self, request, *args, **kwargs):
        try:
            context={'question':Questions.objects.filter(question_slug=kwargs['question_slug']).get()}
            return render(request, self.template_name, context)
        except Questions.DoesNotExist:
            return redirect('/')
   
    def post(self, request, *args, **kwargs):
            try:
                data=request.POST.dict()
                question=Questions.objects.filter(question_slug=kwargs['question_slug']).get()
                if Answers.objects.filter(answer_by = request.user, question=question).exists():
                    context={'question':question, 'error_message':'You have already answered to this question'}
                    return render(request, self.template_name, context)
                Answers.objects.create(answer_by = request.user, question=question, **data)
                return redirect(f'/question/{question.question_slug}/')
            except Questions.DoesNotExist:
                return redirect('/')

        
class SingleAnserView(BaseAuthenticatedView,View):
    template_name = 'question.html'

    def get(self, request, *args, **kwargs):
        resp = kwargs['resp']
        ans_id = kwargs['ans_id']
        count = kwargs['count']
        try:
            question=Questions.objects.filter(question_slug=kwargs['question_slug']).get()
            context={'question':question}
            answer=Answers.objects.get(id=ans_id)
            if str(count) == str(-1):
                if str(resp) == str(1):
                    answer.liked_by.remove(request.user)
                else:
                    answer.disliked_by.remove(request.user)
            elif str(count) == str(1):
                if str(resp) == '1':
                    answer.liked_by.add(request.user)
                    answer.disliked_by.remove(request.user)
                else:
                    answer.disliked_by.add(request.user)
                    answer.liked_by.remove(request.user)
            return redirect(f'/question/{question.question_slug}/')
        except Questions.DoesNotExist:
            return redirect('/')
        except:
            return render(request, self.template_name, context)