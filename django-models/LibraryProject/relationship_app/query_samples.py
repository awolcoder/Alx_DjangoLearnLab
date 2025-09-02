import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_models.settings')
django.setup()

from relationship_app.models import Author, Library

# Query all books by author
author = Author.objects.get(name="J.K. Rowling")
for book in author.books.all():
    print(f"Book by J.K. Rowling: {book.title}")

# List all books in library
library = Library.objects.get(name="Central Library")
for book in library.books.all():
    print(f"Book in library: {book.title}")

# Get librarian of library
print(f"Librarian: {library.librarian.name}")

