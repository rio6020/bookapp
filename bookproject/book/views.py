from django.shortcuts import render
from django.views.generic import ListView,CreateView,DeleteView,UpdateView
from .models import Book
from django.urls import reverse_lazy

class ListBookview(ListView):
    template_name = 'book/book_list.html'
    model = Book

class CreateBookView(CreateView):
    template_name = 'book/book_create.html'
    model = Book
    fields = ('title','purchase_date','thumbnail','read_date')
    success_url = reverse_lazy('list-book')

class DeleteBookView(DeleteView):
    template_name = 'book/book_delete.html'
    model = Book
    success_url = reverse_lazy('list-book')



class UpdateBookView(UpdateView):
    template_name = 'book/book_update.html'
    model = Book
    fields = ('title','purchase_date','thumbnail','read_date')
    success_url = reverse_lazy('list-book')