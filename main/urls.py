from django.urls import path
from .views import *


urlpatterns = [
    path('',principal, name='principal'),
    path('horas',horas, name='horas'),

]