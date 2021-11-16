from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# a view-function is a function which takes in request and yields a response
# request -> response
# request handler


def say_hello(request):
    # Here we could do the following:
    # pull data from database
    # transform data
    # send emails
    # etc.

    x = 1
    y = 2
    return render(request, 'hello.html', {'name': 'Sven'})
