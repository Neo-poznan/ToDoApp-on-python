from django.db import models
from django.db.models import QuerySet
from django.core.exceptions import ValidationError

from users.models import User


class CategoryQuery(QuerySet):

    def GetCustomCategories(self, user):
        # берем сначала все стандартные, а потом категории созданные пользователем
        base = self.filter(is_custom=False)
        custom = self.filter(user=user, is_custom=True) 
        # объединяем их в один queryset
        return base.union(custom)

class Category(models.Model):
    name = models.CharField(max_length=120)
    # строка содержащая цвет прмерно так 'rgba(255, 99, 132, 0.2)' этот цвет будет отображаться на диаграмме
    color = models.CharField(max_length=40)
    is_custom = models.BooleanField(default=True)
    # пользователь создавший категорию
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)

    
    objects = CategoryQuery.as_manager()
    


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
        if not deadline:
            deadline = None
        category_id = data['category']
        category = Category.objects.get(id = category_id)


        if task_list: # если это первая задача пользователя, order будет 0 
            current_last_order = task_list.last().order # получаем order из самого конца списка
            order = current_last_order + 1 # новый таск будет добавляться в конец списка
        else:
            order = 0 
          
        try:
            # добавляем задачу
            self.objects.create(name=name, order=order, 
                deadline=deadline, category=category, user=user)
            return {'success': 'success', 'error': ''}
        except (ValueError, ValidationError) as form_except:
            return {'success': '', 'error': f'{form_except}'}
    
