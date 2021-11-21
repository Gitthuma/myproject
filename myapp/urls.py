# import path that will allow us to add multiple urls in a list
from django.urls import path


# Create a list to hold all the urls
# Create the first url
urlpatterns = [
    path('', views.index, name=index)

]
