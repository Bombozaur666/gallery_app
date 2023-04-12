from django.core.validators import MinValueValidator
from django.db import models
from sites.models import sites


# Create your models here.
class photo(models.Model):
    filename = models.CharField(max_length=255)
    description = models.TextField(max_length=2048)
    filesize = models.IntegerField(default=0)
    edit_date = models.DateTimeField(auto_now=True)
    photo = models.ImageField()
    sort_value = models.IntegerField(default=1, validators=[MinValueValidator(1)])

    class Meta:
        ordering = ('-gallery_photos',)


class gallery(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=2048)
    sort_value = models.IntegerField(default=1, validators=[MinValueValidator(1)])
    private = models.BooleanField(default=True)
    edit_date = models.DateTimeField(auto_now=True)
    site = models.ForeignKey(sites,
                             on_delete=models.CASCADE,
                             related_name='gallery_sites')
    photos = models.ManyToManyField(photo, related_name='gallery_photos')

    class Meta:
        ordering = ('-sort_value',)
