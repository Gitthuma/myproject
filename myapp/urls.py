# import path that will allow us to add multiple urls in a list
# import view to use it in the url
from django.urls import path
from . import views


# Create a list to hold all the urls
# Create the first url
urlpatterns = [
    path('', views.index, name=index)

]
