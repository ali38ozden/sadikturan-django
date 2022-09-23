from turtle import title
from django.db import models

class Blog(models.Model):
    title= models.CharField(max_length=200)
    image= models.CharField(max_length=50)
    description= models.TextField()
    is_acitve= models.BooleanField()
    is_home= models.BooleanField()

    def __str__(self):
        return f"{self.title}"

class Catogory(models.Model):
    name = models.CharField(max_length=150)
    
    def __str__(self):
        return self.name


