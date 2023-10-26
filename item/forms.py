from django import forms

from .models import *

INPUT_CLASSES='w-full px-6 py-4 rounded-xl border'
class Newitemform(forms.ModelForm):
    class Meta:
        model=items
        fields=('category','name','desc','price','image')

        widgets={
            'category':forms.Select(attrs={'class':INPUT_CLASSES}),
            'name':forms.TextInput(attrs={'class':INPUT_CLASSES}),
            'desc':forms.Textarea(attrs={'class':INPUT_CLASSES}),
            'price':forms.TextInput(attrs={'class':INPUT_CLASSES}),
            'image':forms.FileInput(attrs={'class':INPUT_CLASSES}),
        }

class Edititemform(forms.ModelForm):
    class Meta:
        model=items
        fields=('name','desc','price','image','is_sold')

        widgets={
            'name':forms.TextInput(attrs={'class':INPUT_CLASSES}),
            'desc':forms.Textarea(attrs={'class':INPUT_CLASSES}),
            'price':forms.TextInput(attrs={'class':INPUT_CLASSES}),
            'image':forms.FileInput(attrs={'class':INPUT_CLASSES}),
        }