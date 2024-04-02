from django.contrib import admin
from accounts.models import CustomUserModel
from accounts.forms import CustomUserChangeForm , CustomUserCreationForm
from django.contrib.auth.admin import UserAdmin
# Register your models here.
@admin.register(CustomUserModel)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUserModel
    fieldsets = UserAdmin.fieldsets + ((None,{'fields':('age',)}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None,{'fields':('age','email')}),)