from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import * 
from .forms import * 

# Create your views here.

def index(request):
	tasks = Task.objects.all()
	
	form = TaskForm()

	if request.method == "POST":
		form = TaskForm(request.POST)

		if form.is_valid():
			form.save()

		return redirect("/")

	context = {"tasks": tasks, "form": form}

	return render(request, "todo_app/list.html", context)


def updateTask(request, prim_key):
	
	task = Task.objects.get(id=prim_key)

	# instance of the same task so that we can edit it 
	form = TaskForm(instance=task)

	if request.method == "POST":
		form = TaskForm(request.POST, instance=task)

		if form.is_valid():
			form.save()

		return redirect("/")

	context = {"form": form}

	return render(request, "todo_app/update_task.html", context)

def deleteTask(request, prim_key):

	task = Task.objects.get(id=prim_key)

	if request.method == "POST":
		task.delete()
		
		return redirect("/")	

	context = {"task": task}

	return render(request, "todo_app/delete_task.html", context)