from django import forms
from .models import Entry

class EntryForm(forms.ModelForm):

    class Meta:
        model = Entry
        fields = ('title', 'body')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'size': 40}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'rows': 20})
        }
