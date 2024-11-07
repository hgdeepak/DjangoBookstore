from django.db import models


# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    is_active = models.BooleanField(null=False, blank=False, default=True)

    def __str__(self):
        return self.name


class Publisher(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    is_active = models.BooleanField(null=False, blank=False, default=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=250, null=False, blank=False)
    publisher = models.ForeignKey(to=Publisher, on_delete=models.CASCADE)
    author = models.ManyToManyField(to=Author)
    isbn = models.CharField(max_length=13, null=False, blank=False, unique=True)
    description = models.TextField(max_length=300, null=True, blank=True)
    price = models.FloatField(max_length=5, null=False, blank=False)
    is_active = models.BooleanField(null=False, blank=False, default=True)

    def __str__(self):
        return self.title
