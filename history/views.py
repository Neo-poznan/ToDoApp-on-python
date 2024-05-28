import json

from django.views.generic import TemplateView

from history.models import TaskHisoty

class HistoryView(TemplateView):
    template_name = 'history/history.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # передача в контекст истории 
        history = TaskHisoty.objects.filter(user=self.request.user).order_by('deletion_date')
        context['history'] = history.sort_by_date() # вернет словарь, где ключем будет дата, а значением все таски с этой датой удаления
        # передача данных для диаграммы
        date_for_stat = self.kwargs.get('date')
        if date_for_stat: # если нужна статистика по конкретному дню.  date_for_stat передается в ссылке
            objects_for_stats = history.filter(deletion_date=date_for_stat)
            context['chart_data'] = json.dumps(objects_for_stats.get_dataset_for_chart())
            context['selected_date'] = objects_for_stats.first().deletion_date   #   'selected_date' нужен для надписи рядом с диаграммой        
        else: # если за все время
            context['chart_data'] = json.dumps(history.get_dataset_for_chart())
            context['selected_date'] = 'За все время'          

        return context
    
