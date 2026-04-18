from django.shortcuts import render, redirect
from .models import Task

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/task_list.html', {'tasks': tasks})
def task_add(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        if title:
            Task.objects.create(title=title)
            return redirect('task_list')
    return render(request, 'tasks/task_add.html')
