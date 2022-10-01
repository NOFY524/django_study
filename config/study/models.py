from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    phone = models.CharField(max_length=20)
    school = models.CharField(max_length=20)
    grade = models.CharField(max_length=20)
