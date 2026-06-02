from django.db import models

# Create your models here.

class Employees(models.Model):
    Name = models.CharField(max_length=100)
    Position = models.CharField(max_length=100)
    Office = models.CharField(max_length=100)
    Age = models.IntegerField(max_length=3)
    Start_Date = models.DateField()
    Salary = models.IntegerField(max_length=10)

    def __str__(self):
        return self.Name