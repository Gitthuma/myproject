# import http to use in the return statement of the index function
from os import name
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# create an index function that takes requests and will also be referenced by the views module in the urls.py file

# return a HttpResponse
# Change HttpResponse to a render request
# Add a variable to make the program dynamic and send that data to template


def index(request):
    name = "George"
    return render(request, 'index.html', {'name': name})
