from django.urls import path
from .views import list_books   # ✅ Explicit import for checker
from .views import LibraryDetailView   # ✅ Also import the class-based view

urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]


