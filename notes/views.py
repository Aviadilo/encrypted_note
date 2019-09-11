from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from .models import Note, Category
from .forms import NoteCreateForm
from django.urls import reverse_lazy
from cryptography.fernet import Fernet
import base64


def encode_key(key):
    while len(key) % 32 != 0:
        key += b' '
    return base64.urlsafe_b64encode(key)


def encrypt(key, note_text):
    # convert string to bytes
    byte_key = bytes(key, 'utf-8')
    byte_note_text = bytes(note_text, 'utf-8')
    # extend length of byte_key to 32 char and encode it
    padded_key = encode_key(byte_key)
    # make cipher based on padded_key
    cipher = Fernet(padded_key)
    # encrypt the text
    encrypted_text = cipher.encrypt(byte_note_text)
    return str(encrypted_text, 'utf-8')


def decrypt(key, note_text):
    # convert string to bytes
    byte_key = bytes(key, 'utf-8')
    byte_note_text = bytes(note_text, 'utf-8')
    # extend length of byte_key to 32 char and encode it
    padded_key = encode_key(byte_key)
    # make cipher based on padded_key
    cipher = Fernet(padded_key)
    # decrypt the text
    decrypted_text = cipher.decrypt(byte_note_text)
    return str(decrypted_text, 'utf-8')


class NoteList(ListView):
    model = Note
    template_name = 'note_list.html'


class NoteCreate(CreateView):
    model = Note
    template_name = 'note_create.html'
    form_class = NoteCreateForm

    def form_valid(self, form):
        self.object = form.save()
        user_key = self.request.POST.get('password')
        category = self.request.POST.get('category')
        ctg, created = Category.objects.get_or_create(category_name=category, defaults={'category_name': category})
        self.object.category = ctg
        self.object.note_body = encrypt(key=user_key, note_text=self.object.note_body)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('note-list')
