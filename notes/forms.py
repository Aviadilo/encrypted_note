from django import forms
from .models import Note


class NoteCreateForm(forms.ModelForm):
    category = forms.CharField(required=False)
    password = forms.CharField(widget=forms.PasswordInput, label='key for encoding')

    class Meta:
        model = Note
        fields = ['note_body']


class NoteUpdateForm(forms.ModelForm):
    category = forms.CharField(required=False)
    password_for_decode = forms.CharField(widget=forms.PasswordInput, label='enter current key')
    password_for_encode = forms.CharField(widget=forms.PasswordInput, label='enter new key, if you want to change it', required=False)

    class Meta:
        model = Note
        fields = ['note_body']
