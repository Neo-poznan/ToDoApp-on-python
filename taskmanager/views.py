import json

from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View, TemplateView

from taskmanager.models import Task, Category
from taskmanager.color_converter import hex_to_rgba_02, random_hex



class TaskListView(LoginRequiredMixin,TemplateView):
    template_name = 'taskmanager/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task_list'] = Task.objects.filter(user=self.request.user).order_by('order')
        return context
    

class UpdateTaskOrder(View):

    def post(self, request):
        # получаем список текущего расположения задач на странице
        body_unicode = request.body.decode('utf-8')
        body_data = json.loads(body_unicode)
        new_task_list = body_data['order']
        # получаем queryset расположения задач в бд
        current_task_set = Task.objects.filter(user=self.request.user).order_by('order')
        # тут сталкиваемся с проблемой: order_by постоянно сортирует queryset, что будет мешать нормальному сохранению
        # при этом необходимо чтобы он был отсортирован по "order"
        # так что просто перезапишем его в список не изменяя последовательность
        task_list_for_save = list(current_task_set)
        # проходимся сразу по двум спискам
        for order in range(len(new_task_list)):
            task_for_save = task_list_for_save[order]  
            # изменяем в бд значение order на то, которое на странице клиента
            task_for_save.order = new_task_list[order]
            task_for_save.save(update_fields=['order'])

        return JsonResponse({'status': 'ok'})
    

class AddTaskView(View):

    template_name = 'taskmanager/todoadd.html'
    
    def get(self, request):
        context = {'categories': Category.objects.GetCustomCategories(self.request.user)}
        return render(request, self.template_name, context)
    
    def post(self, request):
        body_unicode = request.body.decode('utf-8')
        body_data = json.loads(body_unicode)
        result = Task.AddTask(user=request.user, data=body_data)
        # result это успешный результат или ошибка
        return JsonResponse(result)
    

def delete_task_view(request, task_id):
    Task.objects.get(id=task_id).delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


class CategoryCreationView(View):
    template_name = 'taskmanager/todoaddcategory.html'
      
    def get(self, request):
        context = {'color_val': random_hex()}
        return render(request, self.template_name, context)
    
    def post(self, request):
        body_unicode = request.body.decode('utf-8')
        form = json.loads(body_unicode)
        name = form['name']
        hex = form['color']
        rgba = hex_to_rgba_02(hex) #  переделываем хеш цвета в rgba и добавляем прозрачность 0.2
        Category.objects.create(name=name, color=rgba, user=self.request.user)
        return JsonResponse({'error': '', 'success': 'success'}) 
    

def DeleteCategoryView(request, category_id):
    Category.objects.get(id=category_id).delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


