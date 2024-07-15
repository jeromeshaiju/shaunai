from django.urls import path
from . import views

urlpatterns = [
    path('', views.firstview, name='home'),
    path('process/', views.process_input, name='process-input'),
]