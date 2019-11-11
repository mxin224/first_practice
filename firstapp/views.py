from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def first(request):

    return HttpResponse()

def second(request):

    return HttpResponse()


def third(request):
    print('33333')
    print(1111)
    return HttpResponse(1)
