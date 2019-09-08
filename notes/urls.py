from django.urls import path
from notes.views import *

urlpatterns = [
    path('', NoteList.as_view(), name='note-list'),
    path('create', NoteCreate.as_view(), name='note-create'),
]
