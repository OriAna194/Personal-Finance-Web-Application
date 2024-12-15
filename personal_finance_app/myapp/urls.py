from django.urls import path 
from . import views 

urlpatterns = [ 
    path('', views.home, name='home'), 
    path('expenses/', views.expenses, name='expenses'), 
    path('addGoal/', views.addGoal, name='addGoal'),
    path('updateGoal/<int:pk>', views.updateGoal, name='updateGoal'),
    path('deleteGoal/<int:pk>/', views.deleteGoal, name='deleteGoal'),
    path('addCategory/', views.addCategory, name='addCategory'),
    path('updateCategory/<int:pk>', views.updateCategory, name='updateCategory'), 
    path('deleteCategory/<int:pk>/', views.deleteCategory, name='deleteCategory'), 
    path('expenses/reset/', views.reset_expenses, name='reset_expenses'),
] 