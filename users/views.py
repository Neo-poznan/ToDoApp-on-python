from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import View
from django.contrib.auth import login, authenticate
from django.http import HttpResponseRedirect
from django.contrib import messages

from users.forms import UserLoginForm, UserRegistrationForm


class UserLoginView(LoginView):
    form_class = UserLoginForm
    template_name = 'users/login.html'

    def get_success_url(self):
        return reverse_lazy('taskmanager:index')



class UserRegistrationView(View):
    template_name = 'users/registration.html'
    success_url = reverse_lazy('taskmanager:index')
    extra_context = {'form':UserRegistrationForm()} 

    # если гет
    def get(self, request):
        return render(request, self.template_name, self.extra_context)
    
    # если запрос пост
    def post(self, request):
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save() # создаем юзера
            # достаем из формы данные для авторизации
            username = form.cleaned_data.get('username') 
            password = form.cleaned_data.get('password1')
            # проверяем есть ли юзер в БД
            user = authenticate(username=username, password=password)
            if user:
                login(request,user) # сразу логиним его
                return HttpResponseRedirect(self.success_url)
        # если не получилось зарегистрировать выводим ошибки формы
        messages.error(request, form.errors) 
        return render(request, self.template_name, self.extra_context)
    

class UserLogoutView(LogoutView):
    next_page = reverse_lazy('users:login')

    

    
        



