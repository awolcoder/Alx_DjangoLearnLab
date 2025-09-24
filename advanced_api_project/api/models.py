from django.db import models

class Author(models.Model):
    """
    Author model representing a writer.
    Fields:
        - name: Stores the full name of the author.
    """
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Book(models.Model):
    """
    Book model representing a book.
    Fields:
        - title: The title of the book.
        - publication_year: The year the book was published.
        - author: ForeignKey linking the book to an Author.
    """
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(
        Author, related_name="books", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.title} ({self.publication_year})"
