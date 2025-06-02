from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.cache import cache
from .models import Book

@receiver(post_save, sender=Book)
def cache_book_on_save(sender, instance, **kwargs):
    key = f'book:{instance.id}'
    cache.set(key, {
        'id': instance.id,
        'title': instance.title,
        'author': instance.author,
    }, timeout=3600)  
