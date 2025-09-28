from rest_framework import generics, permissions
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer


# -------------------------
# AUTHOR VIEWS (CRUD)
# -------------------------

# List all authors OR create a new author
class AuthorListCreateView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    # Allow read for everyone, write only for authenticated users
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


# Retrieve, update, or delete a specific author
class AuthorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


# -------------------------
# BOOK VIEWS (CRUD)
# -------------------------

# List all books OR create a new book
class BookListCreateView(generics.ListCreateAPIView):
    """
    GET: Returns a list of all books
    POST: Creates a new book (authenticated users only)
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


# Retrieve, update, or delete a specific book
class BookRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET: Retrieve a single book by ID
    PUT/PATCH: Update book details (authenticated users only)
    DELETE: Delete book (authenticated users only)
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
