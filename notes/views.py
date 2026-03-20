from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from .models import Note
from .forms import NoteForm
from django.core.paginator import Paginator

def note_create(request):
    form = NoteForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('notes:list')
    return render(request, 'notes/create.html', {'form': form})

def note_list(request):
    qs = Note.objects.order_by('-updated_at')
    q = request.GET.get('q')
    tag = request.GET.get('tag')
    if q:
        qs = qs.filter(title__icontains=q) | qs.filter(content__icontains=q)
    if tag:
        qs = qs.filter(tag__iexact=tag)
    paginator = Paginator(qs, 6)
    page = request.GET.get('page')
    notes = paginator.get_page(page)
    return render(request, 'notes/list.html', {'notes': notes, 'q': q, 'tag': tag})

def note_detail(request, pk):
    note = get_object_or_404(Note, pk=pk)
    return render(request, 'notes/detail.html', {'note': note})

def note_edit(request, pk):
    note = get_object_or_404(Note, pk=pk)
    form = NoteForm(request.POST or None, instance=note)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('notes:detail', pk=note.pk)
    return render(request, 'notes/edit.html', {'form': form, 'note': note})

@require_POST
def note_delete(request, pk):
    note = get_object_or_404(Note, pk=pk)
    note.delete()
    return redirect('notes:list')
