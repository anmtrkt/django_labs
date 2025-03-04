import uuid

from django.db import models

class Books(models.Model):
    name = models.CharField(max_length=30)
    author_name = models.CharField(max_length=10)
    author_surname = models.CharField(max_length=20)
    price = models.IntegerField()
    description = models.TextField()
    quantity = models.IntegerField()
    isArchived = models.BooleanField(default=False)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
