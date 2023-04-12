from django.db import models

# Create your models here.


class sites(models.Model):
    name = models.CharField(max_length=255)
