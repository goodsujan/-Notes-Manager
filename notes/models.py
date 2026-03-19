from django.db import models
from django.utils import timezone
from django.urls import reverse

class Note(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    tag = models.CharField(max_length=30, blank=True)
    color = models.CharField(max_length=7, default="#f9f9f9")
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('notes:detail', args=[str(self.id)])
