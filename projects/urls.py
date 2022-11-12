from django.urls import path
from . import views

urlpatterns = [
    path('', views.projects, name="projects"),
    path('create/', views.createProject, name="project_create"),
    path('update/<str:pk>/', views.updateProject, name="project_update"),
    path('delete/<str:pk>/', views.deleteProject, name="project_delete"),
    path('<str:pk>/', views.project, name="project"),
]