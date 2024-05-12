from typing import Dict, Any

from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from app_users.models import Note, User

from app_users.forms import NoteForm


def notes_page(request, id):
    if not request.user.is_authenticated:
        return redirect('login')

    owner = get_object_or_404(User, id=id)

    notes_list = []
    for note in Note.objects.all():
        if note.owner.id == request.user.id:
            notes_list.append(note)

    context = {
        'notes': notes_list,
        'owner': owner
    }

    return render(request, 'app_note/notes.html', context)


def note_create(request, owner_id):
    if request.method == 'POST':
        owner = get_object_or_404(User, id=owner_id)
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.owner = owner
            note.save()
            return redirect('notes', id=owner_id)

    form = NoteForm
    context = {

        'form': form,

    }
    return render(request, 'app_note/create_note.html', context)


def note_update(request, note_id):
    note = get_object_or_404(Note, id=note_id)

    if note.owner != request.user:
        return redirect("home")

    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)

        if form.is_valid():
            form.save()
            return redirect('notes', id=request.user.id)

    form = NoteForm(instance=note)

    context = {
        'form': form,
    }
    return render(request, 'app_note/note_update.html', context)


def note_page(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    if note.owner != request.user:
        return redirect("home")
    context = {
        'note': note
    }
    return render(request, 'app_note/note_form.html', context)


def note_delete(request, note_id):
    owner = request.user
    note = get_object_or_404(Note, id=note_id)
    if note.owner != request.user:
        return redirect("home")
    note.delete()
    return redirect('notes', id=owner.id)