from django.shortcuts import render, redirect
from django.views.generic import (
    ListView, FormView,
)
import requests
from django.urls import reverse
from .forms import LoginForm, ConfirmForm
from django.contrib.auth import authenticate, login
# Create your views here.
def index(request):
    goods = requests.get(
        'http://localhost:8000/api/v1/me/basket-items/',
        headers = {'Authorization': request.session.get('Authorization')}
    ).json().get('results')
    user = authenticate(request.session.get('Authorization').split()[1])
    context = {'goods': goods, 'user': user}
    return render(request, 'pages/index.html', context)

class LoginView(FormView):
    template_name = 'registration/login.html'
    form_class = LoginForm

    def get_success_url(self):
        return reverse('pages:confirm')

    def form_valid(self, form):
        response = requests.post(
            'http://localhost:8000/api/v1/auth/login/',
            form.cleaned_data,
        )
        return super().form_valid(form)

class ConfirmView(FormView):
    template_name = 'registration/confirm.html'
    form_class = ConfirmForm

    def get_success_url(self):
        return reverse('pages:index')

    def form_valid(self, form):
        response = requests.post(
            'http://localhost:8000/api/v1/auth/confirm/',
            form.cleaned_data
        ).json()
        self.request.session['Authorization'] = 'Bearer ' + response.get('access')
        self.request.session['refresh'] = response.get('refresh')
        return super().form_valid(form)
