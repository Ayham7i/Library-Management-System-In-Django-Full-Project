from django.shortcuts import render
from .models import *
from .forms import BookForm,CategoryForm

# Create your views here.

def index(request):

    if request.method == 'POST':
        add_book  = BookForm(request.POST , request.FILES)
        if add_book.is_valid:
            add_book.save()
    





    context = {
        'books': Book.objects.all(),
        'categories':Category.objects.all(),
        'Book_Count': Book.objects.count(),
        'form':BookForm(),
        'formcat':CategoryForm()

    }
    return render(request,'pages/index.html' ,context)

def books(request):
    context = {
        'books': Book.objects.all(),
        'categories':Category.objects.all(),
        'Book_Count': Book.objects.count()

    }
    return render(request, 'pages/book.html',context)
