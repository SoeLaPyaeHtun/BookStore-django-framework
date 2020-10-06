from django.shortcuts import render
from .models import Book, Category

# Create your views here.


def index(request):
    categ = Category.objects.all()

    last_book = Book.objects.order_by('-created_date')[:5]
    return render(request, 'books/index.html', {
        "last_book": last_book,
        "categ": categ
    })


def categ(request, name):
    categ = Category.objects.all()
    cat = Category.objects.get(name=name)

    book_list = Book.objects.filter(Category=cat)
    return render(request, 'books/cat.html', {
        "book_list": book_list,
        "categ": categ,
        "message": "Books isn't avaible"
    })


def detail(request, name):
    book_list = Book.objects.filter(title=name)
    return render(request, 'books/detail.html', {
        "book_list": book_list
    })
