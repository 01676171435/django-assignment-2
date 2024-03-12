from .models import TaskModel
from django.shortcuts import render, redirect
from first_app.forms import TaskForm


def home(request):
    if request.method == 'POST':
        task = TaskForm(request.POST)
        if task.is_valid():
            task.save()
            return redirect('showtasks')

    else:
        task = TaskForm()
    return render(request, 'home.html', {'task': task})


def show_tasks(request):
    tasks = TaskModel.objects.all()
    return render(request, 'show_tasks.html', {'tasks': tasks})


def edit_task(request, Title):
    store = TaskModel.objects.get(taskTitle=Title)
    task = TaskForm(instance=store)
    if request.method == 'POST':
        task = TaskForm(request.POST, instance=store)
        if task.is_valid():
            task.save()
            return redirect('showtasks')
    return render(request, 'home.html', {'task': task})


def delete_task(request, Title):
    store = TaskModel.objects.get(taskTitle=Title).delete()
    return redirect('showtasks')
