# Generated by Django 4.2 on 2023-04-12 15:32

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sites', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.CharField(max_length=255)),
                ('description', models.TextField(max_length=2048)),
                ('filesize', models.IntegerField(default=0)),
                ('edit_date', models.DateTimeField(auto_now=True)),
                ('photo', models.ImageField(upload_to='')),
                ('sort_value', models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1)])),
            ],
            options={
                'ordering': ('-gallery_photos',),
            },
        ),
        migrations.CreateModel(
            name='gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(max_length=2048)),
                ('sort_value', models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1)])),
                ('private', models.BooleanField(default=True)),
                ('edit_date', models.DateTimeField(auto_now=True)),
                ('photos', models.ManyToManyField(related_name='gallery_photos', to='gallery.photo')),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gallery_sites', to='sites.sites')),
            ],
            options={
                'ordering': ('-sort_value',),
            },
        ),
    ]
