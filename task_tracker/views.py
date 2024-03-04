from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'task_tracker/task_list.html', {'tasks': tasks})

def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.priority_color = request.POST.get('priority_color', 'black')
            task.status_color = request.POST.get('status_color', 'black')
            task.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'task_tracker/create_task.html', {'form': form})

def edit_task(request, task_id):
    task = Task.objects.get(id=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            task = form.save(commit=False)
            task.priority_color = request.POST.get('priority_color', 'black')
            task.status_color = request.POST.get('status_color', 'black')
            task.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'task_tracker/edit_task.html', {'form': form})

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'task_tracker/delete_task_confirm.html', {'task': task})
