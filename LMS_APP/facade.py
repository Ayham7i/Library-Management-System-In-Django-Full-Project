from .models import Book, Category
from .forms import BookForm, CategoryForm

class LibraryFacade:
    def __init__(self):
        self.book_form = BookForm
        self.category_form = CategoryForm

    def get_all_books(self):
        return Book.objects.all()

    def get_all_categories(self):
        return Category.objects.all()

    def get_book_count(self, active=None, status=None):
        if active is not None:
            return Book.objects.filter(active=active).count()
        elif status is not None:
            return Book.objects.filter(status=status).count()
        return Book.objects.count()

    def save_book(self, request):
        form = self.book_form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return True
        return False

    def save_category(self, request):
        form = self.category_form(request.POST)
        if form.is_valid():
            form.save()
            return True
        return False

    def get_book_form(self, instance=None):
        return self.book_form(instance=instance)

    def delete_book(self, id):
        book = Book.objects.get(id=id)
        book.delete()
        return True
