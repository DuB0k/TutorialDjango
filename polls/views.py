from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime
from polls.models import Question
from django.template import RequestContext, loader




def home(request):
    return render(request, 'home.html', {'right_now':datetime.utcnow()})

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #template = loader.get_template('polls/index.html')
    #context = RequestContext(request, {
    #    'latest_question_list': latest_question_list,
    #})
    #return HttpResponse(template.render(context))
    ##The same code but usin django.shortcuts
    context = {'latest_question_list':latest_question_list}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(reuqest, question_id):
    response = "you're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." %question_id)
