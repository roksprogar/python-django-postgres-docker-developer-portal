from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginUser, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerUser, name="register"),
    
    path('', views.profiles, name="profiles"),
    path('profiles/<str:pk>/', views.profile, name="profile"),

    path('account/', views.userAccount, name="account"),   
    path('edit-account/', views.editAccount, name="edit_account"),
    
    path('create-skill/', views.createSkill, name="create_skill"),
    path('update-skill/<str:pk>/', views.updateSkill, name="update_skill"),
    path('delete-skill/<str:pk>/', views.deleteSkill, name="delete_skill"),
]
