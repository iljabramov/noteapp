from django.http import HttpResponse
from django.shortcuts import render

def noteList(request):
    return HttpResponse('Note List')
