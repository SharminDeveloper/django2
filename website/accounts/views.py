from django.shortcuts import render
from django.views.generic.edit import CreateView
from accounts.forms import CustomUserCreationForm
from django.urls import reverse_lazy
# Create your views here.
class SignUp(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/sign_up.html'
    