from django.contrib import admin
from .models import Blog,Catogory
# Register your models here.



class BlogAdmin(admin.ModelAdmin):
    list_display = ("title","is_acitve","is_home","slug")
    list_editable = ("is_acitve","is_home")
    search_fields = ("title","description") #arama buttonu ekliyor
    readonly_fields =("slug",)
    
admin.site.register(Blog, BlogAdmin)
admin.site.register(Catogory)