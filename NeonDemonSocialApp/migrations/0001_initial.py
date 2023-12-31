# Generated by Django 3.2.23 on 2023-12-08 10:43

import cloudinary.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('rating', models.IntegerField()),
                ('content', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
        migrations.CreateModel(
            name='UploadImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Uploaded_image', cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image')),
                ('date_uploaded', models.DateField(auto_now_add=True)),
                ('likes', models.ManyToManyField(blank=True, related_name='photo_likes', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-date_uploaded'],
            },
        ),
    ]
