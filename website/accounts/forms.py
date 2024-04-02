from django.contrib.auth.forms import UserCreationForm , UserChangeForm
from accounts.models import CustomUserModel
from django import forms 
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUserModel
        fields = UserCreationForm.Meta.fields + ('email',)
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUserModel
        fields = UserChangeForm.Meta.fields