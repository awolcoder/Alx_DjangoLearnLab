import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.LibraryProject.settings')
django.setup()

from relationship_app.models import Author, Book, Library

author_name = "J.K. Rowling"
library_name = "Central Library"


# 1. Query all books by a specific author using filter()

try:
    author = Author.objects.get(name=author_name)
    books_by_author = Book.objects.filter(author=author)  
    print(f"Books by {author_name}:")
    for book in books_by_author:
        print(f"- {book.title}")
except Author.DoesNotExist:
    print(f"No author found with name '{author_name}'")


# 2. List all books in a specific library

try:
    library = Library.objects.get(name=library_name)
    print(f"\nBooks in {library_name}:")
    for book in library.books.all():
        print(f"- {book.title}")
except Library.DoesNotExist:
    print(f"No library found with name '{library_name}'")


# 3. Retrieve the librarian for the library

try:
    librarian = library.librarian
    print(f"\nLibrarian of {library_name}: {librarian.name}")
except Library.librarian.RelatedObjectDoesNotExist:
    print(f"{library_name} does not have a librarian assigned")

