from django.urls import path 
from . import views

urlpatterns = [
    path('', views.index),
    path('add_book', views.add_book),
    path('books/<int:book_id>', views.books),
    path('authors', views.authors),
    path('new_authors', views.new_authors),
    path('author/<int:author_id>', views.author),
    path('add_author', views.add_author),
    path('books/<int:book_id>/assign', views.new_author),
    path('author/<int:author_id>/assign', views.new_book)
]