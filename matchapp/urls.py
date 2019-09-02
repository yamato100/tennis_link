from django.urls import path
from .views import signupfunc, loginfunc, listfunc, logoutfunc, detailfunc, BoardCreate, topfunc, mypagefunc



urlpatterns = [
    path('signup/', signupfunc, name='signup'),
    path('login/', loginfunc, name='login'),
    path('list/', listfunc, name='list'),
    path('logout/', logoutfunc, name='logout'),
    path('detail/<int:pk>', detailfunc, name='detail'),
    path('create/', BoardCreate.as_view(), name='create'),
    path('mypage/', mypagefunc, name='mypage'),
    path('', topfunc, name='top'),
]