from django.urls import path
from .views import MyLogin, MyRegist, NoteList, NoteCreate, redirect_view
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('',  redirect_view, name="index"),
    path('home',NoteList.as_view(), name = 'notes'),
    path('login',MyLogin.as_view(), name = 'login'),
    path('regist',MyRegist.as_view(), name = 'regist'),
    path('logout',LogoutView.as_view(next_page='login'), name = 'logout'),
    path('add',NoteCreate.as_view(), name = 'add'),
]