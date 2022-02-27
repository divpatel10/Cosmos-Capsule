from django.shortcuts import render
from django.http import HttpResponse

# request handler

# create a view 
def say_hello(req):
    return render(req, 'debug.html')
