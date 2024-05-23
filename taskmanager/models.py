from django.db import models

from users.models import User


class Category(models.Model):
    name = models.CharField(max_length=120)
    # строка содержащая цвет прмерно так 'rgba(255, 99, 132, 0.2)' этот цвет будет отображаться на диаграмме
    color = models.CharField(max_length=40)
    is_custom = models.BooleanField(default=True)
    # пользователь создавший категорию
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)

class Task(models.Model):
    name = models.CharField(max_length=250)
    # порядок таска в списке дел
    order = models.IntegerField()
    deadline = models.DateField(blank=True, null=True)
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}. Порядок {self.order}'

    @classmethod
    def AddTask(self, user, data):
        # получаем список дел пользователя в текущем порядке
        task_list = self.objects.filter(user=user).order_by('order')
        # достаем данные из формы
        name = data['name']
        deadline = data['deadline']
        category_name = data['catagory']
        # получаем категорию по названию
        category = Category.objects.get(name=category_name)
        # получаем order из самого конца списка
        current_last_order = task_list.last()
        # новый таск будет добавляться в конец списка
        order = current_last_order + 1
        # добавляем
        self.objects.create(name=name, order=order, deadline=deadline, category=category, user=user)

        
