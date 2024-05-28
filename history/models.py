from django.db import models

from taskmanager.models import Category
from users.models import User

class HistoryQuery(models.QuerySet):

    def get_dataset_for_chart(self):
        categories_colors_dict = {}    # берем именно словари потому что так гораздо легче прибавлять задачу к кол. задач нужной категории
        tasks_in_category_dict = {}    # а еще в них не будет дубликатов, при этом сохраняя последовательность
        for task in self:
            categories_colors_dict[task.category] = task.category.color
            if task.category in tasks_in_category_dict.keys():
                tasks_in_category_dict[task.category] += 1
            else:
                tasks_in_category_dict[task.category] = 1
                # этот генератор просто получает список названий всех категорий в том же порядке
        categories = list(category.name for category in categories_colors_dict.keys())
        categories_colors = list(categories_colors_dict.values())
        tasks_in_category = list(tasks_in_category_dict.values())
        return {'categories': categories, 'data': tasks_in_category, 'colors': categories_colors}
    
    def sort_by_date(self):

        data = {}
        for task in self:
            if not task.deletion_date in data.keys():
                data[task.deletion_date] = [task]
            else:
                data[task.deletion_date].append(task)
        return data



class TaskHisoty(models.Model):
    task_name = models.CharField(max_length=250)
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE)
    deletion_date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)

    objects = HistoryQuery.as_manager()


