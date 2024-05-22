from django.db import models

from users.models import User


class Category(models.Model):
    name = models.CharField(max_length=120)
    # строка содержащая цвет прмерно так 'rgba(255, 99, 132, 0.2)' этот цвет будет отображаться на диаграмме
    color = models.CharField(max_length=40)

class Task(models.Model):
    name = models.CharField(max_length=250)
    order = models.IntegerField()
    deadline = models.DateField(blank=True)
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)