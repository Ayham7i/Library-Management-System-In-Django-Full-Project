from django import forms
from .models import Book , Category

class BookForm(forms.ModelForm): 
    class Meta:
        model = Book
        fields = [
            'title',
            'author',
            'book_photo',
            'author_photo',
            'pages',
            'price',
            'rental_price_day',
            'rental_period',
            'status',
            'category',
        ]