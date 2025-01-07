from django.db import models

# Create your models here.


class UniqueNumbers(models.Model):
    number = models.BigIntegerField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

