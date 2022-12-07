from django.urls import path
from . import views

urlpatterns = [
    path(r'^$', views.index, name='index'),
    path(r'about/', views.about, name='about'),
    path(r'data/', views.db_operations, name='db_operations'),
    path(r'present/', views.data_visualization, name='data_visualization'),
]
