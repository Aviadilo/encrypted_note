from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from .models import Note, Category
from .forms import NoteCreateForm
from django.urls import reverse_lazy
from .func import *


class NoteList(ListView):
    model = Category
    template_name = 'note_list.html'


class NoteEncoded(DetailView):
    model = Note
    template_name = 'note_detail.html'


class NoteCreate(CreateView):
    model = Note
    template_name = 'note_create.html'
    form_class = NoteCreateForm

    def form_valid(self, form):
        self.object = form.save()
        user_key = self.request.POST.get('password')
        self.object.category = set_category(self.request.POST.get('category'))
        self.object.note_body = encrypt(key=user_key, note_text=self.object.note_body)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('note-list')
