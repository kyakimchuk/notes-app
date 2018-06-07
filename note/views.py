from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from note.models import Note
import re


class AllNotesList(ListView):
    context_object_name = 'notes_list'
    template_name = 'note/note_list.html'
    model = Note

    def get_queryset(self):
        def sort_by_unique_words_count(note):
            # removing punctuation marks from note
            temp = re.sub(r'[,;:"!?\.\[\]\(\)]', ' ', note.note_text)
            # removing single quotes (leaving the apostrophes)
            temp = re.sub(r'[^a-zA-Zа-яА-Я]\'|\'[^a-zA-Zа-яА-Я]|^\'|\'$', ' ', temp)
            count = len(set(temp.split()))
            return count
        notes_list = Note.objects.all()
        notes_list = sorted(notes_list, key=lambda n: sort_by_unique_words_count(n))
        return notes_list


class AddNote(CreateView):
    model = Note
    fields = ['note_text']
    success_url = reverse_lazy('success')


def success(request):
    return render(request, 'note/success.html')