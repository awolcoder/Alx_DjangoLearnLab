from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
#from .views import (
#    list_books,
#   LibraryDetailView,
#   register_view,
#    add_book,
#    edit_book,
#    delete_book,
#    admin_view,
#    librarian_view,
#    member_view
#)

urlpatterns = [
    # Book views
    path('books/', list_books, name='list_books'),
    path('book/add/', add_book, name='add_book'),
    path('book/edit/<int:pk>/', edit_book, name='edit_book'),
    path('book/delete/<int:pk>/', delete_book, name='delete_book'),

    # Library view
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),

    # Authentication
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', register_view, name='register'),

    # Role-based views
    path('admin-view/', admin_view, name='admin_view'),
    path('librarian-view/', librarian_view, name='librarian_view'),
    path('member-view/', member_view, name='member_view'),
]

