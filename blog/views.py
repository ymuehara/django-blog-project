from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'YuriU',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'June 29th, 2020'
    },
    {
        'author': 'PancakeU',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'June 30th, 2020'
    }
]

# function returns what the user will see when sent this route


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)
# return HttpResponse("<h1>Blog Home</h1>")


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
