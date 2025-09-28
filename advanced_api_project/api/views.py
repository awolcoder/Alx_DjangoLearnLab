from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer


# -------------------------
# AUTHOR VIEWS (CRUD)
# -------------------------

class AuthorListCreateView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class AuthorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


# -------------------------
# BOOK VIEWS (CRUD + Filtering/Searching/Ordering)
# -------------------------

class BookListCreateView(generics.ListCreateAPIView):
    """
    GET: Returns a list of all books with filtering, searching, and ordering.
    POST: Creates a new book (authenticated users only)
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # Enable filtering, search, and ordering
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    # Fields for filtering via query params, e.g., ?publication_year=2020
    filterset_fields = ['title', 'author__name', 'publication_year']

    # Fields for text search via ?search=keyword
    search_fields = ['title', 'author__name']

    # Fields for ordering via ?ordering=title or ?ordering=-publication_year
    ordering_fields = ['title', 'publication_year', 'author__name']
    ordering = ['title']  # default ordering

class BookRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
