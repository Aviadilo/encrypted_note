from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from .models import Note, Category
from .forms import NoteCreateForm, NoteUpdateForm
from django.urls import reverse_lazy
from .func import *
from django.http import Http404


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
        self.object.category = set_category(self)
        self.object.note_body = encrypt(key=user_key, note_text=self.object.note_body)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('note-list')


class NoteDecoded(UpdateView):
    model = Note
    template_name = 'note_update.html'
    form_class = NoteUpdateForm

    def get_object(self, queryset=None):
        obj = super().get_object()
        user_key = self.request.POST.get('password_for_decode')
        obj.note_body = decrypt(key=user_key, note_text=obj.note_body)
        if obj.note_body == 'Invalid key':
            raise Http404()
        else:
            return obj

    def get_form_kwargs_formmixin(self):
        kwargs = {
            'initial': self.get_initial(),
            'prefix': self.get_prefix(),
        }
        if self.request.method in ('POST', 'PUT') and self.request.POST.get('update_and_encode'):
            kwargs.update({
                'data': self.request.POST,
                'files': self.request.FILES,
            })
        return kwargs

    def get_form_kwargs(self):
        kwargs = self.get_form_kwargs_formmixin()
        if hasattr(self, 'object'):
            kwargs.update({'instance': self.object})
        return kwargs

    def form_valid(self, form):
        self.object = form.save()
        user_key = set_key(self)
        self.object.category = set_category(self)
        self.object.note_body = encrypt(key=user_key, note_text=self.object.note_body)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('note-list')
