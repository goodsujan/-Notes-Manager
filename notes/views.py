from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.http import HttpResponse
import csv
from .models import Note
from .forms import NoteForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

def _popular_tags():
    """Return up to 20 distinct non-empty tags with their most recent color."""
    return (
        Note.objects
        .exclude(tag='')
        .values('tag', 'color')
        .distinct()
        .order_by('-tag')[:20]
    )

def note_create(request):
    form = NoteForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        note = form.save(commit=False)
        if request.user.is_authenticated:
            note.user = request.user
        else:
            from django.contrib.auth.models import User
            note.user = User.objects.first() or User.objects.create_user('admin', 'admin@example.com', 'adminpass')
        note.save()
        return redirect('notes:list')
    return render(request, 'notes/create.html', {
        'form': form,
        'popular_tags': _popular_tags(),
    })

def note_list(request):
    qs = Note.objects.all().order_by('-updated_at')
    q = request.GET.get('q')
    tag = request.GET.get('tag')
    if q:
        qs = qs.filter(title__icontains=q) | qs.filter(content__icontains=q)
    if tag:
        qs = qs.filter(tag__iexact=tag)
    paginator = Paginator(qs, 6)
    page = request.GET.get('page')
    notes = paginator.get_page(page)
    return render(request, 'notes/list.html', {
        'notes': notes,
        'q': q,
        'tag': tag,
        'popular_tags': _popular_tags(),
    })

def note_detail(request, pk):
    note = get_object_or_404(Note, pk=pk)
    return render(request, 'notes/detail.html', {'note': note})

def note_edit(request, pk):
    note = get_object_or_404(Note, pk=pk)
    form = NoteForm(request.POST or None, instance=note)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('notes:detail', pk=note.pk)
    return render(request, 'notes/edit.html', {
        'form': form,
        'note': note,
        'popular_tags': _popular_tags(),
    })

@require_POST
def note_delete(request, pk):
    note = get_object_or_404(Note, pk=pk)
    note.delete()
    return redirect('notes:list')

def export_notes_csv(request):
    notes = Note.objects.all().order_by('-updated_at')
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="notes_export.csv"'
    writer = csv.writer(response)
    writer.writerow(['id','title','tag','color','created_at','updated_at','content'])
    for n in notes:
        writer.writerow([n.id, n.title, n.tag, n.color, n.created_at, n.updated_at, n.content])
    return response
