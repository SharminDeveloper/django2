from django.urls import path
from pages import views
urlpatterns = [
    path('',views.Home.as_view(),name='home')
]
