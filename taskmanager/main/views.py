from django.shortcuts import render, redirect, HttpResponse
from .models import Task
from .forms import TaskForm
from django.contrib import admin


# Create your views here.
def index(request):
    tasks = Task.objects.order_by('id')
    return render(request, 'main/index.html', {'title': 'Главная страница сайта', 'tasks': tasks})


def edit(request):
    tasks = Task.objects.order_by('id')
    return render(request, 'main/edit.html', {'title': 'Главная страница сайта', 'tasks': tasks})


def admin(request):
    pass


def about(request):
    return render(request, 'main/about.html')


def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была неверной'
    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', context)


def idk(request):
    return redirect('https://ya.ru/')
