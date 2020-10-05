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
