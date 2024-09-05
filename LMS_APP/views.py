from django.shortcuts import redirect, render, get_object_or_404
from .facade import LibraryFacade

# Create a single instance of the facade to be used in all views
library_facade = LibraryFacade()

def index(request):
    if request.method == 'POST':
        library_facade.save_book(request)
        library_facade.save_category(request)

    context = {
        'books': library_facade.get_all_books(),
        'categories': library_facade.get_all_categories(),
        'form': library_facade.get_book_form(),
        'formcat': library_facade.category_form(),
        'Book_Count': library_facade.get_book_count(active=True),
        'BookSold': library_facade.get_book_count(status='Sold'),
        'BookRental': library_facade.get_book_count(status='Rental'),
        'BookAvailable': library_facade.get_book_count(status='Available'),
    }
    return render(request, 'pages/index.html', context)

def books(request):
    context = {
        'books': library_facade.get_all_books(),
        'categories': library_facade.get_all_categories(),
        'Book_Count': library_facade.get_book_count(),
    }
    return render(request, 'pages/book.html', context)

def update(request, id):
    book_instance = get_object_or_404(Book, id=id)
    if request.method == 'POST':
        form = library_facade.get_book_form(instance=book_instance)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = library_facade.get_book_form(instance=book_instance)
    
    context = {
        'form': form,
    }
    return render(request, 'pages/update.html', context)

def delete(request, id):
    if request.method == 'POST':
        library_facade.delete_book(id)
        return redirect('/')
    return render(request, 'pages/delete.html')
