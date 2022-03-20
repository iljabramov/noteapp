from django.http import HttpResponse
from django.shortcuts import redirect
from django.views.generic.list import ListView
from .models import Note
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin

def redirect_view(request):
    response = redirect('/home')
    return response

class NoteList(LoginRequiredMixin, ListView):
    model = Note
    context_object_name = 'notes'

class NoteCreate(LoginRequiredMixin, CreateView):
    model = Note
    fields = '__all__'
    success_url = reverse_lazy('notes')

class MyLogin(LoginView):
    template_name = 'mynoteapp/login.html'
    fields = '__all__'
    redirect_authenticated_user = True
    def get_success_url(self):
        return reverse_lazy('notes')


    