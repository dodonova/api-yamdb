# Generated by Django 3.2 on 2023-09-23 07:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0009_alter_title_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='title',
            name='rating',
        ),
    ]
