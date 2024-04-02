from django.urls import path 
from accounts import views
urlpatterns = [
    path('sign_up/',views.SignUp.as_view(),name='sign_up'),
]
