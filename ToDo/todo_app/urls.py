from . import views
from django.urls import path 


urlpatterns = [
	path('', views.index, name="list"),
	path("update_task/<str:prim_key>", views.updateTask, name="update_task"),
	path("delete_task/<str:prim_key>", views.deleteTask, name="delete_task"),
]