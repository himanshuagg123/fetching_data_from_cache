from django.urls import path
from .views import get_book_by_id

urlpatterns = [
    path('book/<int:book_id>/', get_book_by_id, name='get_book_by_id'),
]
