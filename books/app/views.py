from django.shortcuts import render
from . import models
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def home(request):
    return HttpResponse("My home")

def all_books(request):
    books = models.Book.objects.all()
    return HttpResponse(books)


def index(request):
    return HttpResponse("Hello, world.")
def all_books(request):
    books = models.Book.objects.all()
    context = {
        'books': books,
    }
    return render(request, 'all_books.html', {'context': context})


# Create your views here.
