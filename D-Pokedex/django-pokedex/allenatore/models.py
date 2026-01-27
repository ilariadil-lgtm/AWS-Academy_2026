from django.db import models
import uuid

# Create your models here.

class Allenatore(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200, unique=True)
    surname = models.CharField(max_length=200, unique=True)
    