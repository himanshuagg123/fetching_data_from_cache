from django.http import JsonResponse
from django.core.cache import cache
from .models import Book

def get_book_by_id(request, book_id):
    key = f'book:{book_id}'
    book_data = cache.get(key)

    if book_data:
        print("Data fetched from cache")
    else:
        print("Data fetched from database")
        try:
            book = Book.objects.get(id=book_id)
            book_data = {'id': book.id, 'title': book.title, 'author': book.author}
            cache.set(key, book_data, timeout=None)
        except Book.DoesNotExist:
            return JsonResponse({'error': 'Book not found'}, status=404)

    return JsonResponse(book_data)
