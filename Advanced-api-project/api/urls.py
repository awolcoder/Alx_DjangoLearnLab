from django.urls import path
from .views import (
    AuthorListCreateView, AuthorRetrieveUpdateDestroyView,
    BookListCreateView, BookRetrieveUpdateDestroyView
)

urlpatterns = [
    path('authors/', AuthorListCreateView.as_view(), name='author-list-create'),
    path('authors/<int:pk>/', AuthorRetrieveUpdateDestroyView.as_view(), name='author-detail'),
    path('books/', BookListCreateView.as_view(), name='book-list-create'),
    path('books/<int:pk>/', BookRetrieveUpdateDestroyView.as_view(), name='book-detail'),
]
