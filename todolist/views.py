from django.shortcuts import render
from todolist.models import ToDoList
from todolist.forms import ToDoListForms
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.urls import reverse
from django.core import serializers

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
    # Ambil form pembuatan user
    form = UserCreationForm()
    
    # Handle jika request merupakan POST
    if request.method == "POST":
        
        # Jika form yang diberikan valid, maka simpan user yang disubmit kemudian
        # Redirect ke page login
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')

    # Kembalikan render halaman register
    context = {'form': form}
    return render(request, 'register.html', context)


def login_user(request):
    # Handle jika request merupakan POST
    if request.method == 'POST':
        # Autentikasi user berdasarkan username dan password yang dimasukkan
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        # Handle jika user ditemukan
        if user is not None:
            login(request, user)  # melakukan login terlebih dahulu
            response = HttpResponseRedirect(
                reverse("todolist:show_todolist"))  # membuat response
            # membuat cookie last_login dan menambahkannya ke dalam response
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        
        # Jika tidak ditemukan, berikan info
        else:
            messages.info(request, 'Username atau Password salah!')
    
    # Render halaman login.html
    context = {}
    return render(request, 'login.html', context)


def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response


@login_required(login_url='/todolist/login/')
def add_todolist(request):
    # Pastikan user sudah log in
    if request.user.is_authenticated:
        # Ambil form-nya dari http request
        form = ToDoListForms(request.POST)
        
        # Handle jika form valid dan method request adl. POST
        if request.method == 'POST' and form.is_valid():
            # Ambil title & description dari form, buat task baru, lalu redirect
            # ke halaman utama
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            task_baru = ToDoList.objects.create(title=title, description=description,
                                                user=request.user, date=datetime.date.today())
            return redirect('todolist:show_todolist')

        # Render halaman add task
        context = {
            'form': form,
        }
        return render(request, 'addToDoList.html', context)
    else:
        return redirect('todolist:login')

@login_required(login_url='/todolist/login/')
def add_todolist_ajax(request):
    # Pastikan user sudah log in
    if request.user.is_authenticated:
        # Ambil form-nya dari http request
        form = ToDoListForms(request.POST)
        response_data = {}
        
        # Handle jika form valid dan method request adl. POST
        if request.method == 'POST' and form.is_valid():
            # Ambil title & description dari form, buat task baru, lalu redirect
            # ke halaman utama
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            task_baru = ToDoList.objects.create(title=title, description=description,
                                                user=request.user, date=datetime.date.today())
            response_data['title'] = title
            response_data['description'] = description
            response_data['date'] = datetime.date.today()
            return JsonResponse(response_data);

        # Render halaman add task
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
        return JsonResponse({'msg':'success'})
    else:
        return redirect('todolist:login')


@login_required(login_url='/todolist/login/')
def toggle_completion(request, id):
    if request.user.is_authenticated:
        task = ToDoList.objects.get(id=id)
        task.is_finished = not task.is_finished
        task.save()
        return JsonResponse({'msg':'success'})
    else:
        return redirect('todolist:login')

@login_required(login_url='/todolist/login/')
def get_json(request):
    todolist = ToDoList.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", todolist), content_type="application/json")