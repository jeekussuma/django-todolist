
from django.urls import path, include

from . import views
urlpatterns = [
    path('', views.index, name="list"),
    path('updatetask/<str:pk>', views.updateTask,  name="updatetask"),
    path('deletetask/<str:pk>', views.deleteTask, name="deletetask"),



]
