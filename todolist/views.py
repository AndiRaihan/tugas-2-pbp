from django.shortcuts import render
from todolist.models import ToDoList
from todolist.forms import ToDoListForms
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.


@login_required(login_url='/todolist/login/')
def show_todolist(request):
    if request.user.is_authenticated:
        todolist = ToDoList.objects.filter(user=request.user)
        last_login_info = request.COOKIES.get('last_login', 'not found')
        if (last_login_info == 'not found'):
            return redirect('todolist:login')
        context = {
            'list_kerjaan': todolist,
            'user_name': request.user.username,
            'last_login': request.COOKIES.get('last_login', 'not found'),
        }
        return render(request, 'todolist.html', context)

    else:
        return redirect('todolist:login')


def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')

    context = {'form': form}
    return render(request, 'register.html', context)


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)  # melakukan login terlebih dahulu
            response = HttpResponseRedirect(
                reverse("todolist:show_todolist"))  # membuat response
            # membuat cookie last_login dan menambahkannya ke dalam response
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)


def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response


@login_required(login_url='/todolist/login/')
def add_todolist(request):
    if request.user.is_authenticated:
        form = ToDoListForms(request.POST)
        if request.method == 'POST' and form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            task_baru = ToDoList.objects.create(title=title, description=description,
                                                user=request.user, date=datetime.date.today())
            return redirect('todolist:show_todolist')

        context = {
            'form': form,
        }
        return render(request, 'addToDoList.html', context)
    else:
        return redirect('todolist:login')


@login_required(login_url='/todolist/login/')
def delete(request, id):
    if request.user.is_authenticated:
        task = ToDoList.objects.get(id=id)
        task.delete()
        return redirect('todolist:show_todolist')
    else:
        return redirect('todolist:login')


@login_required(login_url='/todolist/login/')
def toggle_completion(request, id):
    if request.user.is_authenticated:
        task = ToDoList.objects.get(id=id)
        task.is_finished = not task.is_finished
        task.save()
        return redirect('todolist:show_todolist')
    else:
        return redirect('todolist:login')
