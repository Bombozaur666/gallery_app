from django.db import models
from sites.models import sites
from django.core.validators import MaxLengthValidator


# Create your models here.
class subjects(models.Model):
    site = models.ForeignKey(sites, on_delete=models.CASCADE)
    name = models.CharField(max_length=64,
                            blank=False,
                            null=False)
    row_id = models.IntegerField(null=True, blank=True)
    row_prefix = models.CharField(max_length=64, null=True, blank=True)

