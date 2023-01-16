# myapp/models.py

from django.db import models


class Document(models.Model):
    file = models.FileField()
    title = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    # test
