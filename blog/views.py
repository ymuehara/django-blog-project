from django.shortcuts import render
from django.http import HttpResponse
from .models import Post  # dot means  from the models file in the current package


# function returns what the user will see when sent this route


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)
# return HttpResponse("<h1>Blog Home</h1>")


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
