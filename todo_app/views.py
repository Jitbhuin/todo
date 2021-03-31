from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Todo
from .forms import UserRegisterForm, LoginForm, TaskForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required


# for login
def login_user(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = LoginForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            print(request.POST)
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Successfully Logged In")
                redirect_url = request.GET.get('next', 'todo_app:add')
                return redirect(redirect_url)
            else:
                messages.error(request, "Invalid credentials! Please try again")
                return redirect("todo_app:login_user")
    # if a GET (or any other method) we'll create a blank form
    else:
        form = LoginForm()
    return render(request, 'todo_app/login.html', {'form': form})


# for signing up user
def signup_user(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            user = User.objects.create_user(
                username=username, password=password, email=email)
            user.save()
            messages.success(request, "Your profie has been successfully created")
            return redirect('todo_app:login_user')
    else:
        form = UserRegisterForm()
    data_for_frontend = {
        'form': form
    }
    return render(request, 'todo_app/signup.html', data_for_frontend)


# for logging out user
def logout_user(request):
    logout(request)
    return redirect('todo_app:login_user')


# for add items in todo list
@login_required(login_url='todo_app:login_user')
def add(request):
    todo_list = Todo.objects.filter(user=request.user).order_by('is_todo_completed')
    if request.method == "POST":
        todo_title = request.POST['todo_title']
        todo_list = Todo(
            user=request.user,
            todo_title=todo_title
        )
        todo_list.save()
        return redirect('todo_app:add')
    data_for_frontend = {
        'todo_list': todo_list,
    }
    return render(request, 'todo_app/add.html', data_for_frontend)


# for editing item in todo list
@login_required(login_url='todo_app:login_user')
def edit(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    form = TaskForm(request.POST or None, instance=todo)
    if form.is_valid():
        form.save()
        # form = TaskForm()
        return redirect('todo_app:add')
    data_for_frontend = {
        'form': form,
    }
    print(request.POST)
    return render(request, 'todo_app/edit.html', data_for_frontend)


# for deleting item in todo list
def delete(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    # if request.method == "POST":
    #     todo.delete()
    #     return redirect("todo_app:add")
    # data_for_frontend = {
    #     'todo': todo,
    # }
    # return render(request, 'todo_app/delete.html', data_for_frontend)
    todo.delete()
    return redirect('todo_app:add')


# def confirm_delete(request, todo_id):
#     todo = Todo.objects.get(id=todo_id)
#     todo.delete()
#     return render(request, 'todo_app/add.html')


def about(request):
    return render(request, 'todo_app/about.html')


@login_required(login_url='todo_app:login_user')
def profile(request):
    print(request.user.profile.whatever)
    HttpResponse({'ll'})

