from django.shortcuts import render
from .models import Book
from django.core.cache import cache

def book_list(request):
    books = cache.get('all_books')

    if not books:
        print("Fetching from DB")
        books = list(Book.objects.all())
        cache.set('all_books', books, 30) 
    else:
        print("Fetching from Cache")

    return render(request, 'books/book_list.html', {'books': books})
