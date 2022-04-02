from django.shortcuts import render
from django.http.response import HttpResponse
from django.shortcuts import render


# def index(request):
#     return HttpResponse('OK!')


def test(request):
    return HttpResponse('test')
