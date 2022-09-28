from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from todolist.models import Task
from todolist.forms import TaskForm
from django.contrib.auth.models import User


# Create your views here.

@login_required(login_url='/todolist/login/')
def show_todolist(request):
    data_task = Task.objects.filter(user=request.user)
    context = {
        'list_task': data_task,
    }
    return render(request, "todolist.html", context)


def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('todolist:show_todolist')
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    return redirect('todolist:login')

def add_task(request):
    form = TaskForm()

    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user=User.objects.get(username=request.user.username)
            task.save()
            return redirect('todolist:show_todolist')
    
    context = {'form':form}
    return render(request, 'add-task.html', context)

def change_status(request):
    if request.method == "POST":
        task = Task.objects.get(id=request.POST["id"])
        task.status = not(task.status)
        task.save()
    return redirect('todolist:show_todolist')

def delete_task(request):
    if request.method == "POST":
        task = Task.objects.get(id=request.POST["id"])
        task.delete()
    return redirect('todolist:show_todolist')

