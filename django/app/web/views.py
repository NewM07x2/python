from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import json
words = ['Japanese', 'English', 'French']


def index(repuest):
    list = []
    params = {
        'name': 'masato',
        'age': 30,
        'word': ''
    }
    for word in words:
        print(word)
        params['word']=word
        list.append(params)

    json_str = json.dumps(list, ensure_ascii=False, indent=2)
    return HttpResponse(json_str)
