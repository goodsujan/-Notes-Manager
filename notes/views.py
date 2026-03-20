from django.shortcuts import render, redirect, get_object_or_404
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
