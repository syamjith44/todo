
from django.urls import path
from . import views
urlpatterns = [

    path('', views.toDoList, name='toDoList'),
    path('update/<int:task_id>/', views.update, name='update'),
    path('delete/<int:task_id>/', views.delete, name='delete'),

]