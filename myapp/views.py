# import http to use in the return statement of the index function
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# create an index function that takes requests and will also be referenced by the views module in the urls.py file


def index(request):
    pass
