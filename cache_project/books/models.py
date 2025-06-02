from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)  # title of the book field "char type"
    author = models.CharField(max_length=100) # autthor field "char type"
    

    def __str__(self):
        return self.title
