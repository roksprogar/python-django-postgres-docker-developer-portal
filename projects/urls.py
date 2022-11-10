from django.urls import path
from . import views

urlpatterns = [
    path('projects/', views.projects, name="projects"),
    path('projects/create/', views.createProject, name="project_create"),
    path('projects/update/<str:pk>/', views.updateProject, name="project_update"),
    path('projects/delete/<str:pk>/', views.deleteProject, name="project_delete"),
    path('projects/<str:pk>/', views.project, name="project"),
]