from django.db import models
from django.contrib.auth.models import User as AuthUser
import uuid


class Matricola(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    matricola = models.TextField() # specificare il metodo di creazione di questa matricola
    user = models.OneToOneField(AuthUser, on_delete=models.CASCADE, related_name="matricola")

    class Meta:
        db_table = "matricolas"