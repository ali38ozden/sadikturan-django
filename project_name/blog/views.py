from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.


def index(request):
    return render(request,"blog_tmp/index.html")

def blogs(request):
    return render(request, "blog_tmp/blogs.html")

def blogs_details(request,number):
    return render(request, "blog_tmp/blogs-details.html", {
        "html_number":number
        })