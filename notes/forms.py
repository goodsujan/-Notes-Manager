from django import forms
from .models import Note

class NoteForm(forms.ModelForm):
    color = forms.CharField(widget=forms.TextInput(attrs={'type': 'color'}), required=False)

    class Meta:
        model = Note
        fields = ['title', 'content', 'tag', 'color']
        widgets = {
            'content': forms.Textarea(attrs={'rows':4}),
        }
