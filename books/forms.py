from django import forms

from .models import Book

class PostForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = ('author', 'title','summary', 'owner',
                  'temp_owner','is_read','quantity','wish_list')