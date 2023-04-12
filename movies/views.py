# views are just functions
from django.http import HttpResponse
from django.shortcuts import render

data = {
    'movies':[
        {
            'id': 5,
            'title': 'jaws',
            'year' : '1995'
        },
        {
            'id': 6,
            'title': 'sharknado',
            'year' : '2010'
        },
        {
            'id': 7,
            'title': 'The Meg',
            'year' : '2020'
        }
    ]
}

def movies(request):
    return render(request, 'movies/movies.html', data) #render() takes 3 arguments
    #return HttpResponse("Hello There")

def home(request):
    return HttpResponse("Home Page")