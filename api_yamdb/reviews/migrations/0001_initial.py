# Generated by Django 3.2 on 2023-09-23 14:09

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, validators=[django.core.validators.MaxLengthValidator(limit_value=200)])),
                ('slug', models.SlugField(unique=True, validators=[django.core.validators.MaxLengthValidator(50), django.core.validators.RegexValidator(regex='^[-a-zA-Z0-9_]+$')])),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('pub_date', models.DateTimeField(auto_now_add=True, db_index=True)),
            ],
            options={
                'ordering': ('pub_date',),
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, validators=[django.core.validators.MaxLengthValidator(limit_value=200)])),
                ('slug', models.SlugField(unique=True, validators=[django.core.validators.MaxLengthValidator(50), django.core.validators.RegexValidator(regex='^[-a-zA-Z0-9_]+$')])),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='GenreTitle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('score', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(1, '< 1'), django.core.validators.MaxValueValidator(10, '> 10')])),
                ('pub_date', models.DateTimeField(auto_now_add=True, db_index=True)),
            ],
            options={
                'ordering': ('pub_date',),
            },
        ),
        migrations.CreateModel(
            name='Title',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('year', models.PositiveSmallIntegerField()),
                ('description', models.TextField(blank=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='category', to='reviews.category')),
                ('genre', models.ManyToManyField(through='reviews.GenreTitle', to='reviews.Genre')),
            ],
            options={
                'ordering': ('-id',),
            },
        ),
    ]
