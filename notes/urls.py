from django.urls import path
from notes.views import *

urlpatterns = [
    path('', NoteList.as_view(), name='note-list'),
    path('encoded/<int:pk>', NoteEncoded.as_view(), name='note-encoded-detail'),
    path('create', NoteCreate.as_view(), name='note-create'),
    path('decoded/<int:pk>', NoteDecoded.as_view(), name='note-decoded-update'),
]
