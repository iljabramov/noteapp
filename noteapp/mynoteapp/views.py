from django.http import HttpResponse
from django.shortcuts import redirect
from django.views.generic.list import ListView
from .models import Note
from django.views.generic.edit import CreateView, FormView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login



def redirect_view(request):
    response = redirect('/home')
    return response

class NoteList(LoginRequiredMixin, ListView):
    model = Note
    context_object_name = 'notes'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['notes'] = context['notes'].filter(user=self.request.user)
        return context


class NoteCreate(LoginRequiredMixin, CreateView):
    model = Note
    fields = ['title','description']
    success_url = reverse_lazy('notes')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class MyLogin(LoginView):
    template_name = 'mynoteapp/login.html'
    fields = '__all__'
    redirect_authenticated_user = True
    def get_success_url(self):
        return reverse_lazy('notes')


class MyRegist(FormView):
    template_name = 'mynoteapp/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('notes')
    
    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request,user)
        return super(MyRegist, self).form_valid(form)