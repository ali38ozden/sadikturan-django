from django.shortcuts import render
from blog.models import Blog

# Create your views here.


# data={
#     "blogs":[
#         {
#             "id":1,
#             "title":"komple web geliştirme",
#             "image":"hacker.jpg",
#             "is_active":True,
#             "home_active":True,
#             "description":"cok iyi bir kurs"
#         },
#         {
#             "id":2,
#             "title":"kamera",
#             "image":"basit.jpg",
#             "is_active":True,
#             "home_active":True,
#             "description":"cok orta bir kurs"
#         },
#         {
#             "id":3,
#             "title":"yazlım desetek",
#             "image":"hacker.jpg",
#             "is_active":True,
#             "home_active":False,
#             "description":"cok kötü bir kurs"
#         },
#         {
#             "id":4,
#             "title":"Bos",
#             "image":"basit.jpg",
#             "is_active":False,
#             "home_active":True,
#             "description":"cok kötü bir kurs"
#         }
#     ]
# }


def index(request):
    context={
        "blogs" : Blog.objects.filter(is_acitve = True, is_home= False),
        "fuls" : Blog.objects.all()
    }
    return render(request,"blog_tmp/index.html", context)


def blogs(request):
    context={
        "blogs": Blog.objects.filter(is_acitve = True),
        "fuls" : Blog.objects.all()
    }
    return render(request, "blog_tmp/blogs.html", context)


def blogs_details(request,slug):
    blog = Blog.objects.get(slug=slug)
    return render(request, "blog_tmp/blogs-details.html", {
        "blog":blog,
        "fuls" : Blog.objects.all()
        })