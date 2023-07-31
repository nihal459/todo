from django.shortcuts import get_object_or_404, redirect, render
from . models import *
# Create your views here.

def home(request):
    tasks = Task.objects.filter(is_completed = False).order_by('-updated_at')
    completed_tasks = Task.objects.filter(is_completed =True)

    context = {
        'tasks':tasks,
        'completed_tasks':completed_tasks
    }
    return render(request, "home.html", context)


def addTask(request):
    a = request.POST.get("task")
    task = Task.objects.create(task=a)
    return redirect('home')

def mark_as_done(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = True
    task.save()
    return redirect('home')

def mark_as_undone(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = False
    task.save()
    return redirect('home')


def edit_task(request, pk):
    get_task = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        new_task = request.POST['task']
        get_task.task = new_task
        get_task.save()
        return redirect('home')
    else:
        context = {
            'get_task':get_task,
        }
        return render(request, 'edit_task.html', context)
    


def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('home')
