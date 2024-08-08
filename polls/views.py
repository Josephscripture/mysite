from django.shortcuts import render
from django.http import HttpResponse
from .models import(Question)
from .models import(Choice)
def index(request):
    return render(request,"polls/index.html")

# def index(request):
#     questions=Question.objects.all()
#     question_text=[question.question_text for question in questions]
#     return HttpResponse(question_text)

# # Create your views here.
# def mychoice(request):
#     choices = Choice.objects.all()
#     choice_text=[choice.choice_text for choice in choices]
#     return HttpResponse(choice_text)


