from django.urls import path
from .views import MyLogin, NoteList, NoteCreate, redirect_view
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('',  redirect_view, name="index"),
    path('home',NoteList.as_view(), name = 'notes'),
    path('login',MyLogin.as_view(), name = 'login'),
    path('logout',LogoutView.as_view(next_page='login'), name = 'logout'),
    path('add',NoteCreate.as_view(), name = 'add'),
]