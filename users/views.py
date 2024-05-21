from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.views.generic import View


from users.forms import UserLoginForm, UserRegistrationForm

class UserLoginView(LoginView):
    form_class = UserLoginForm
    template_name = 'users/login.html'
    success_url = 'taskmanager/index.html'


class UserRegistrationView(View):
    template_name = 'users/registration.html'
    success_url = 'taskmanager/index.html'
    form_class = UserRegistrationForm()

    def get(self, request):
        context = {'form':self.form_class}
        return render(request, self.template_name, context)



