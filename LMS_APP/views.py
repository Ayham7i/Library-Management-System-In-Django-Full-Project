from django.shortcuts import render
from .models import *
from .forms import BookForm

# Create your views here.

def index(request):
    context = {
        'books': Book.objects.all(),
        'categories':Category.objects.all(),
        'Book_Count': Book.objects.count(),
        'form':BookForm()

    }
    return render(request,'pages/index.html' ,context)

def books(request):
    context = {
        'books': Book.objects.all(),
        'categories':Category.objects.all(),
        'Book_Count': Book.objects.count()

    }
    return render(request, 'pages/book.html',context)
