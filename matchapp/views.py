from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import TennisModel
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, TemplateView
from django.urls import reverse_lazy

# Create your views here.

def signupfunc(request):
    if request.method == 'POST':
        username2 = request.POST['username']
        password2 = request.POST['password']
        try:
            User.objects.get(username=username2)
            return render(request, 'matchapp/signup.html', {'error':'このユーザー名は登録されています'})
        except:
            user = User.objects.create_user(username2, '', password2)
            return render(request, 'matchapp/signup.html')
    return render(request, 'matchapp/signup.html')

def loginfunc(request):
    if request.method == 'POST':
        username2 = request.POST['username']
        password2 = request.POST['password']
        user = authenticate(request, username=username2, password=password2)
        if user is not None:
            login(request, user)
            return redirect('matchapp/list')
        else:
            return render(request, 'matchapp/login.html')
    return render(request, 'matchapp/login.html')

def listfunc(request):
    object_list = TennisModel.objects.all()
    return render(request, 'matchapp/list.html', {'object_list':object_list})

def logoutfunc(request):
    logout(request)
    return redirect('login')

@login_required
def detailfunc(request, pk):
    object = TennisModel.objects.get(pk=pk)
    return render(request, 'matchapp/detail.html', {'object':object})

class BoardCreate(CreateView):
    template_name = 'matchapp/create.html'
    model =TennisModel
    fields = ('title', 'content', 'date', 'time', 'place', 'author')
    success_url = reverse_lazy('list')

def topfunc(request):
    object_list = TennisModel.objects.all()[:]
#    reverse_object_list = reversed(object_list)
    object_new = list(reversed(object_list))[:3]   #モデルを最後に作った順にする
    return render(request, 'matchapp/top.html', {'object_list':object_new})
    # return render(request, 'matchapp/top.html')

@login_required
def mypagefunc(request):
    return render(request, 'matchapp/mypage.html')
  