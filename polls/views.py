from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    name = "Lam Duong"
    favorite = ["AB6ix","Wanna One", "Twice", "Black Pink"]
    context = {"name":name, "kpop": favorite }
    return render(request, "polls/index.html", context)
