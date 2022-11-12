from django.urls import path
from . import views

urlpatterns = [
    path('', views.profiles, name="profiles"),
    path('profiles/<str:pk>/', views.profile, name="profile"),
]
