from django.test import TestCase
from django.urls import reverse
from .models import Note

class NoteModelTest(TestCase):
    def test_create_note(self):
        n = Note.objects.create(title="Test", content="abc")
        self.assertEqual(Note.objects.count(), 1)
        self.assertEqual(n.title, "Test")

class NoteViewTests(TestCase):
    def test_list_view(self):
        Note.objects.create(title="A", content="one")
        resp = self.client.get(reverse('notes:list'))
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, "A")
