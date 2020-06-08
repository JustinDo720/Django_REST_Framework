from django.db import models

# Create your models here.


class Dog(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class ProgrammingLanguage(models.Model):
    languages_names = models.CharField(max_length=50)

    def __str__(self):
        return self.languages_names
