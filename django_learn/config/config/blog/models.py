from django.db import models

# Create your models here.
class blog(models.Model):
    text = models.TextField()