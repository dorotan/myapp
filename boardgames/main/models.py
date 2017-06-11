from datetime import datetime
from django.db import models

# Create your models here.

class Boardgames(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    id = models.FloatField()
    def __str__(self):
        return self.title