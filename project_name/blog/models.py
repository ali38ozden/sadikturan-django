from django.db import models
from django.utils.text import slugify


class Blog(models.Model):
    title = models.CharField(max_length=200)
    image = models.CharField(max_length=50)
    description = models.TextField()
    is_acitve = models.BooleanField()
    is_home = models.BooleanField()
    slug = models.SlugField(null=False, blank=True, unique=True, db_index=True, editable=False) #unique ==> tekrar eden değer olmasın, db_index ==> her bir değerin bir indexi olsun, default => istediğin bir değer atar blank => doldurması zorunlu alaın iptal eder

    def __str__(self):
        return f"{self.title}"

    def save(self, *args, **kwarg):
        self.slug = slugify(self.title)
        super().save(*args, **kwarg)

class Catogory(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(null=False, blank=True, unique=True, db_index=True, editable=False)

    def __str__(self):
        return f"{self.name}"

    def save(self, *args, **kwarg):
        self.slug = slugify(self.name)
        super().save(*args, **kwarg)



