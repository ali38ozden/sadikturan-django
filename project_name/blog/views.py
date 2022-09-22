from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse("Main Page")

def blogs(request):
    return HttpResponse("Blogs Page")

def blogs_details(request,number):
    return HttpResponse("Blogs :"+str(number))
