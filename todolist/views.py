from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import toDoLists, toDoListItem


def current_user(request):
    current_user = None
    if request.user.is_authenticated:
        current_user = request.user
    else:
        current_user = None
    return{
        'current_user': current_user,
    }


def register(request):
    if request.method == 'POST':
        email = request.POST['email']
        full_name = request.POST['full_name']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if not full_name:
            messages.info(
                request, 'İsim-Soyisim alanı doldurulması gereken bir alandır.')
        elif not email:
            messages.info(
                request, 'Mail alanı doldurulması gereken bir alandır.')
        elif len(password1) < 6:
            messages.info(request, 'Şifreniz en az 6 karakterden oluşmalıdır.')
        elif len(full_name) < 5:
            messages.info(
                request, 'İsim Soyisim en az 5 karakterden oluşmalıdır.')
        elif User.objects.filter(email=email):
            messages.error(
                request, 'Email adresiniz daha önce başka bir kullanıcı tarafından kullanılmıştır.')

        else:
            if password1 == password2:
                user = User.objects.create_user(
                    first_name=full_name, username=email, email=email, password=password1)
                user.save()
                return render(request, 'todolist/login.html')
            else:
                messages.info(request, 'Şifreleriniz birbiri ile eşleşmiyor.')
        return render(request, 'todolist/register.html')
    else:
        return render(request, 'todolist/register.html')


def login(request):
    if request.method == 'POST':
        uEmail = request.POST['email']
        uPassword = request.POST['password']
        if uEmail == '':
            messages.warning(request, 'Kayıtlı Mail adresini giriniz.')
        elif uPassword == '':
            messages.warning(request, 'Kayıtlı şifrenizi giriniz.')
        else:
            user = authenticate(request, username=uEmail, password=uPassword)
            if user is not None:
                auth.login(request, user)
                return redirect('todolist')
            else:
                messages.error(request, 'Mail adresiniz yada şifreniz hatalı!')
        return redirect('login')
    else:
        return render(request, 'todolist/login.html')


def logout(request):
    auth.logout(request)
    return redirect('login')


# this method using for list all to do list for current user
def todolist(request):
    cToDoLists = toDoLists.objects.none()
    cToDoListItem = toDoListItem.objects.none()
    if not request.user.is_staff:
        current_user = request.user
        cToDoLists = toDoLists.objects.filter(user=current_user)
        cToDoListItem = toDoListItem.objects.all()
    context = {
        'cToDoLists': cToDoLists,
        'cToDoListItem': cToDoListItem,
    }
    return render(request, 'todolist/todolist.html', context)


# this method using for create a new to do list with user and list_name parameters
def addtodo(request):
    if request.method == 'POST':
        current_user = request.user
        list_name = request.POST['list_name']
        todolist = toDoLists.objects.create(
            user=current_user, list_name=list_name)
        return redirect('todolist')
    return render(request, 'todolist/todolist.html')


# delete specific todolist from users' lists
def deleteToDo(request, id):
    toDoLists.objects.filter(id=id).delete()
    return redirect('todolist')


def addItem(request):
    if request.method == 'POST':
        todolist_name = request.POST['toDo']
        todolist_object = toDoLists.objects.get(list_name=todolist_name)
        item_name = request.POST['item_name']
        description = request.POST['description']
        dead_line = request.POST['deadline']
        created_item = toDoListItem.objects.create(toDoList=todolist_object,
                                                   item_name=item_name, description=description, dead_line=dead_line)
        return redirect('todolist')

    return render(request, 'todolist/todolist.html')
