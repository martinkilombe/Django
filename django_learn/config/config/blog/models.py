from django.db import models
from django.utils import timezone

# Create your models here.
class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.content[:20]  # Show first 20 characters in admin