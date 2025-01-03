# from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    # should we see once we go to Home page
    # return HttpResponse("Hello World! I'm #.")
    return render(request, 'home.html')

def about(request):
    # should we see once we go to About page
    # return HttpResponse("My About page.")
    return render(request, 'about.html')


