from django.urls import path
from . import views

urlpatterns = [
    path('consultation/', views.create_consultation, name='create-consultation'),
    path('cases/', views.list_cases, name='list-cases'),
    path('clients/', views.list_clients, name='list-clients'),
]
