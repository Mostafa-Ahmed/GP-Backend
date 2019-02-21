from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.generic import View


class Registration(UserCreationForm, View):
    template_name = 'accounts/registration_form.html'
    form = UserCreationForm()

    def get(self, request):
        return render(request, self.template_name, {'form': self.form})

    def post(self, request):
        self.form = UserCreationForm(request.POST)
        if self.form.is_valid():
            user = self.form.save()
            login(request, user)
            return redirect('classifier:all-images')
        else:
            return render(request, self.template_name, {'form': self.form})


class Login(View):
    template_name = 'accounts/login_form.html'
    form = AuthenticationForm()

    def post(self, request):
        self.form = AuthenticationForm(data=request.POST)
        if self.form.is_valid():
            user = self.form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            return redirect('classifier:all-images')
        else:
            return render(request, self.template_name, {'form': self.form})

    def get(self, request):
        self.form = AuthenticationForm()
        return render(request, self.template_name, {'form': self.form})


class Logout(View):
    template_name = ''

    def post(self, request):
        logout(request)
        return redirect('classifier:all-images')
