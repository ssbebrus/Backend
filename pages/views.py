from symtable import Class

from django.shortcuts import render, redirect
from django.views.generic import (
    ListView, FormView, CreateView
)
import requests
from django.urls import reverse
from .forms import LoginForm, ConfirmForm
from django.contrib.auth import authenticate, login
from api.models import Good
# Create your views here.
def index(request):
    goods = requests.get(
        'http://localhost:8000/api/v1/goods/',
        headers = {'Authorization': request.session.get('Authorization')}
    ).json().get('results')
    user = authenticate(request.session.get('Authorization'))
    context = {'goods': goods, 'user': user}
    return render(request, 'pages/index.html', context)


class CreateGoodView(CreateView):
    model = Good
    fields = '__all__'
    template_name = 'pages/good_create.html'
    success_url = '/'

    def form_valid(self, form):
        response = requests.post(
            'http://localhost:8000/api/v1/goods/',
            form.cleaned_data,
            headers = {'Authorization': self.request.session.get('Authorization')}
        )
        return super().form_valid(form)


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
