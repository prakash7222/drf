from django.db import models

# Create your models here.


class greet(models.Model):
    first_name = models.CharField(max_length=50)

class Book(models.Model):
    title = models.CharField(max_length = 30)
    author = models.CharField(max_length = 40)
    pdf = models.FileField(upload_to = 'books/pdfs/')
    def __str__(self):
        return self.title
class Product(models.Model):
    tit = models.CharField(max_length = 30)
    description = models.TextField(blank = True,null = True)
    price  = models.DecimalField(max_digits=10, decimal_places=2)
    summary = models.TextField(blank = False,null = False)
    features = models.BooleanField()
    name = models.CharField(max_length = 30)
    def __str__(self):
        return self.tit