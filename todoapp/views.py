from django.shortcuts import redirect, render
from . models import *
# Create your views here.

def home(request):
    tasks = Task.objects.filter(is_completed = False).order_by('-updated_at')
    context = {'tasks':tasks}
    return render(request, "home.html", context)


def addTask(request):
    a = request.POST.get("task")
    task = Task.objects.create(task=a)
    return redirect('home')

