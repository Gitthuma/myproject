# import http to use in the return statement of the index function
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# create an index function that takes requests and will also be referenced by the views module in the urls.py file

# return a HttpResponse
# Change HttpResponse to a render request


def index(request):
    return render(request, 'index.html')
