# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
def index(request):
    context = {
        'time' : strftime('%Y-%m-%d %H:%M %p', gmtime())
    }
    print context
    return render(request, 'Current_Time/index.html', context)

def test(request):
    response = "Hello I am TEST!"
    return HttpResponse(response)