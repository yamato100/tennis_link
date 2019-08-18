from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import TennisModel
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.urls import reverse_lazy

# Create your views here.

def signupfunc(request):
    if request.method == 'POST':
        username2 = request.POST['username']
        password2 = request.POST['password']
        try:
            User.objects.get(username=username2)
            return render(request, 'signup.html', {'error':'このユーザー名は登録されています'})
        except:
            user = User.objects.create_user(username2, '', password2)
            return render(request, 'signup.html')
    return render(request, 'signup.html')

def loginfunc(request):
    if request.method == 'POST':
        username2 = request.POST['username']
        password2 = request.POST['password']
        user = authenticate(request, username=username2, password=password2)
        if user is not None:
            login(request, user)
            return redirect('list')
        else:
            return render(request, 'login.html')
    return render(request, 'login.html')

@login_required
def listfunc(request):
    object_list = TennisModel.objects.all()
    return render(request, 'list.html', {'object_list':object_list})

def logoutfunc(request):
    logout(request)
    return redirect('login')

def detailfunc(request, pk):
    object = TennisModel.objects.get(pk=pk)
    return render(request, 'detail.html', {'object':object})

class BoardCreate(CreateView):
    template_name = 'create.html'
    model =TennisModel
    fields = ('title', 'content', 'time', 'place', 'author')
    success_url = reverse_lazy('list')

def topfunc(request):
    object_list = TennisModel.objects.all()[:]
#    reverse_object_list = reversed(object_list)
    object_new = list(reversed(object_list))[:3]   #モデルを最後に作った順にする
    return render(request, 'top.html', {'object_list':object_new})