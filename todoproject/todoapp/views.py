from django.shortcuts import render, redirect
from .models import Task


def toDoList(request, ):
    tasks = Task.objects.all()
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('desc')
        task = Task(title=title, desc=description)
        task.save()

    return render(request, 'index.html', {'task': tasks, })


def delete(request, task_id):
    if request.method == "POST":
        task = Task.objects.get(id=task_id)
        task.delete()
        return redirect('/')
    return render(request, 'delete.html', )


def update(request, task_id):
    task = Task.objects.get(id=task_id)

    if request.method == "POST":
        task.title = request.POST.get('title')
        task.desc = request.POST.get('description')
        task.save()
        return redirect('/')
    return render(request, 'update.html')
