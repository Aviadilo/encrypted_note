from django import forms
from .models import Note


class NoteCreateForm(forms.ModelForm):
    category = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput, help_text='key for encoding')

    class Meta:
        model = Note
        fields = ['note_body']
