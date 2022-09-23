from django.contrib import admin
from .models import Blog,Catogory
# Register your models here.



class BlogAdmin(admin.ModelAdmin):
    list_display = ("title","is_acitve","is_home")
    list_editable = ("is_acitve","is_home")
    
admin.site.register(Blog, BlogAdmin)
admin.site.register(Catogory)