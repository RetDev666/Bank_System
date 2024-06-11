from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('central_offices/', views.central_offices, name='central_offices'),
    path('branches/', views.branches, name='branches'),
    path('clients/', views.clients, name='clients'),
    path('accounts/', views.accounts, name='accounts'),
]
