import json


from django.shortcuts import render
from django.views.generic import View



class TaskListView(View):
    template = 'taskmanager/index.html'
    extra_context = {}

    def get(self, request):
        
        return render(request, self.template, self.extra_context)
    

class UpdateTaskOrder(View):
    template = 'taskmanager/index.html'
    extra_context = {}
   
    def post(self, request):

        body_unicode = request.body.decode('utf-8')
        body_data = json.loads(body_unicode)
        print(body_data)

        return render(request, self.template, self.extra_context)