# Generated by Django 4.2 on 2023-04-28 21:30

from django.db import migrations
import pyuploadcare.dj.models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_alter_blog_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='image',
            field=pyuploadcare.dj.models.ImageField(blank=True, null=True),
        ),
    ]
