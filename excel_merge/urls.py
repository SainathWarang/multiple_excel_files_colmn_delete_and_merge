from django.urls import path
from . import views

urlpatterns = [
    path('', views.combine_excel, name='combine_excel'),
]
