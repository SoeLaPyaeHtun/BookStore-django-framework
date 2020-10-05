from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=64)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=64)
    author = models.CharField(max_length=64)
    summary = models.TextField(max_length=255, blank=True, null=True)
    price = models.FloatField()
    Category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, default=None, blank=True, null=True)
    image = models.ImageField(
        upload_to="books/img/", blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
