from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name=''),
    path('<int:pk>/', views.checklist_detail, name='checklist_detail'),
    path('checklist_delete/<int:pk>/', views.checklist_delete, name='checklist_delete'),
    path('task_complete/<int:checklist_pk>/<int:item_pk>/', views.task_complete, name='task_complete'),
    path('task_delete/<int:checklist_pk>/<int:item_pk>/', views.task_delete, name='task_delete'),

]