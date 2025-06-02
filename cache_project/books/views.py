from django.http import JsonResponse
from django.core.cache import cache
from .models import Book

def get_book_by_id(request, book_id):
    # Create a unique cache key for the book based on its ID
    key = f'book:{book_id}'cd 
    
    # Try to get the book data from the cache using the cache key
    book_data = cache.get(key)

    if book_data:
        # If book_data exists in cache, it means data was fetched from cache
        print("Data fetched from cache")
    else:
        # If not found in cache, fetch the data from the database
        print("Data fetched from database")
        try:
            # data fetching from the database
            book = Book.objects.get(id=book_id)
            
            
            book_data = {'id': book.id, 'title': book.title, 'author': book.author}
            
            # Store the book data in cache with no expiration (timeout=None)
            cache.set(key, book_data, timeout=None)
            
        except Book.DoesNotExist:
            # If the book with the given ID does not exist, return 404 error as JSON response
            return JsonResponse({'error': 'Book not found'}, status=404)

    # Return the book data as a JSON response
    return JsonResponse(book_data)
