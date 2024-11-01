from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from .models import Book
from .forms import PostForm


def book_list(request):
    #books = Book.objects.all()
    #books = Book.objects.order_by('author')
    books = Book.objects.filter(wish_list='disabled').order_by('author')
    return render(request, 'books/book_list.html', {'books': books})


def book_detail(request,pk):
    book = get_object_or_404(Book,pk=pk)
    return render(request, 'books/book_detail.html', {'book': book})

@login_required
def book_edit(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.author = request.user
            book.save()
            #return redirect('book_list', pk=book.pk)
            return redirect('book_list')
    form = PostForm()
    return render(request, 'books/book_edit.html', {'form' : form})
