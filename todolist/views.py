from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from todolist.models import Task
from todolist.forms import TaskForm
import json
from django.http import HttpResponse, JsonResponse
from django.core import serializers



@login_required(login_url='/todolist/login/')
def show_task(request):
    task_data = Task.objects.filter(user=request.user)
    context = {
        'list_task' : task_data,
        'last_login' : request.COOKIES['last_login']
    }
    return render(request, 'todolist.html', context)

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
            login(request, user) # melakukan login terlebih dahulu
            response = HttpResponseRedirect(reverse("todolist:show_task")) # membuat response
            response.set_cookie('last_login', str(datetime.datetime.now())) # membuat cookie last_login dan menambahkannya ke dalam response
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

@login_required(login_url='/todolist/login/')
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response

@login_required(login_url='/todolist/login/')
def create_task(request):
    form = TaskForm()

    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            messages.success(request, 'Berhasil membuat task!')
            return redirect('todolist:show_task')

    context = {'form': form}
    return render(request, 'create_task.html', context)

@login_required(login_url='/todolist/login/')
def update_task(request, id):
    task_list = Task.objects.filter(id=id)
    task = task_list[0]
    task.is_finished = not task.is_finished
    task.save()
    return redirect('todolist:show_todolist_ajax')

@login_required(login_url='/todolist/login/')
def delete_task(request, id):
    Task.objects.filter(id=id).delete()
    return redirect('todolist:show_todolist_ajax')

@login_required(login_url='/todolist/login/')
def show_todolist_ajax(request):
    task_list = Task.objects.all()
    context = {
    'list_task': task_list,
    'last_login': request.COOKIES['last_login']
    }
    return render(request, "todolist_ajax.html", context)


def post_ajax_todolist(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']

        ins = Task(title=title, description=description)
        ins.save()

        data = {
            "message" : 'Submitted!'
        }
        json_obj = json.dumps(data, indent = 4)

        return JsonResponse(json.loads(json_obj))
    return render(request, "create_task.html")

def show_json(request):
    data = Task.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_json_by_id(request, id):
    data = Task.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")