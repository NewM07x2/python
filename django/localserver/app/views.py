# coding: utf-8
from email.policy import default
from django.shortcuts import render
import django_filters
from rest_framework import viewsets, filters
# Create your views here.


def index(request):
    return render(request, 'app/index.html')


def file(request):
    text = 'OK'
    return render(request, 'app/file.html', context={'value': text})


def home(request):
    text = 'home.html'
    testList = ['タンパク質', '糖質', '脂質', 'ビタミン']
    test_map = {
        'name': 'masato',
        'age': 27
    }
    add = 'add'
    upper = 'abc'
    default_text = 'def'
    cut_text = 'cut_text'
    text_length = 'test1234'
    result = {
        'file_name': text,
        'test_list': testList,
        'test_detail': test_map,
        'add':add,
        'upper':upper,
        'default_text':default_text,
        'cut_text':cut_text,
        'text_length': text_length,
        'number': '1234567890',
        'url': 'https://www.google.com/'
    }
    return render(request, 'app/home.html', context=result)


def sample1(request):
    return render(request, 'app/sample1.html')


def sample2(request):
    return render(request, 'app/sample2.html')
