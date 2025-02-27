from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from todo.models import TODOO
from django.contrib.auth import authenticate, login, logout
from todo import models
from django.contrib.auth.decorators import login_required

# Create your views here.




def signup(request):
    # return HttpResponse("Hello, world. You'r at the todo index.")

    if request.method == 'POST':
        fnm = request.POST.get('fnm')
        emailid = request.POST.get('emailid')
        pwd = request.POST.get('pwd')
        print(fnm, emailid, pwd)
        my_user = User.objects.create_user(fnm, emailid, pwd)
        my_user.save()
        return redirect('/todo/login')
    return render(request, "signup.html")


def user_login(request):
    if request.method == 'POST':
        fnm = request.POST.get('fnm')
        pwd = request.POST.get('pwd')
        print(fnm, pwd)
        userr = authenticate(request, username=fnm, password=pwd)
        if userr is not None:
            login(request, userr)
            return redirect('/todo/todopage')
        else:
            return redirect('/todo/login')
        
    return render(request, "login.html")


@login_required(login_url='/todo/login')
def todo_pg(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        print(title)
        obj = models.TODOO(title= title, user= request.user)
        obj.save()
        res = models.TODOO.objects.filter(user= request.user).order_by('-date')
        return redirect('/todo/todopage', {'res': res})
    
    res = models.TODOO.objects.filter(user= request.user).order_by('-date')
    return render(request, 'todos.html', {"res":res})


def signout(request):
    logout(request)
    return redirect('/todo/login')




@login_required(login_url='/todo/login')
def edit_todo(request, srno):
    if request.method == 'POST':
        title = request.POST.get('title')
        print(title)
        obj = models.TODOO.objects.get(srno=srno)
        obj.title = title
        obj.save()
        return redirect('/todo/todopage')

    obj = models.TODOO.objects.get(srno=srno)
    return render(request, 'edit_todo.html', {'obj': obj})


@login_required(login_url='/todo/login')
def delete_todo(request, srno):
    obj = models.TODOO.objects.get(srno=srno)
    obj.delete()
    return redirect('/todo/todopage')