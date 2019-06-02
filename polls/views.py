from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Question
# Create your views here.
def index(request):
    name = "Lam Duong"
    favorite = ["AB6ix","Wanna One", "Twice", "Black Pink"]
    context = {"name":name, "kpop": favorite }
    return render(request, "polls/index.html", context)

def viewList(request):
    questionList = Question.objects.all()
    context = {"questions": questionList}
    return render(request, 'polls/question-list.html', context)

def detailView(request, question_id):
    question = Question.objects.get(pk=question_id)
    context = {"detailQuestion":question}
    return render(request,'polls/detail-question.html', context)

def vote(request, question_id):
    question = Question.objects.get(pk=question_id)
    try:
        answerValue = request.POST["choice"]
        vote_num = question.choice_set.get(pk=answerValue)
    except:
        HttpResponse("no choice valid")
    vote_num.vote = vote_num.vote + 1
    vote_num.save()
    return render(request, 'polls/results.html', {"question":question})


