from django.shortcuts import render, redirect
from .models import Book, Author

def index(request):
    context = {
        "books": Book.objects.all()
    }
    return render(request, 'index.html', context)

def add_book(request):
    if request.method == "POST":
        Book.objects.create(
            title = request.POST['title'],
            desc = request.POST['desc']
        )
    return redirect ('/')

def books(request, book_id):
    book = Book.objects.get(id=book_id)
    context = {
        "book": book,
        "authors": Author.objects.exclude(books__id=book_id)
    }
    return render(request, 'books.html', context)

def authors(request):
    context = {
        'authors': Author.objects.all()
    }
    return render(request, 'authors.html', context)

def new_authors(request):
    
    return render(request, 'authors', context)

def author(request, author_id):
    author = Author.objects.get(id=author_id)
    context = {
        "author": author,
        "books": Book.objects.exclude(authors__id = author_id),
    }
    return render(request, 'author.html', context)

def add_author(request):
    if request.method == "POST":
        Author.objects.create(
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            notes=request.POST['notes']
        )
    return redirect('/authors')

def new_author(request, book_id):
    book = Book.objects.get(id=book_id)
    author = Author.objects.get(id=request.POST['author_id'])
    book.authors.add(author)
    return redirect(f'/books/{book_id}')

def new_book(request, author_id):
    book = Book.objects.get(id = request.POST['book_id'])
    author = Author.objects.get(id=author_id)
    book.authors.add(author)
    return redirect(f'/author/{author_id}')
