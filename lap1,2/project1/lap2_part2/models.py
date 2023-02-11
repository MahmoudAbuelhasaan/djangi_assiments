from django.db import models

class Book(models.Model):
    name = models.CharField(max_length=100)
    id = models.CharField(max_length=100, primary_key=True)
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.name