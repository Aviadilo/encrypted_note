from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from .models import Note
from .forms import NoteForm
from django.urls import reverse_lazy


class NoteList(ListView):
    model = Note
    template_name = 'note_list.html'


class NoteCreate(CreateView):
    model = Note
    template_name = 'note_create.html'
    form_class = NoteForm

    def get_success_url(self):
        return reverse_lazy('note-list')
