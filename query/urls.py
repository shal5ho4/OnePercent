from django.urls import path
from . import views

app_name = 'query'
  
urlpatterns = [
  path('create/', views.query_form, name='create'),
  path('create/check/', views.query_form, name='check'),
  path('confirmation/', views.query_form, name='confirmation'),
]