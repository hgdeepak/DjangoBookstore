# Generated by Django 5.1.2 on 2024-10-31 13:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('isbn', models.CharField(max_length=13)),
                ('description', models.TextField(blank=True, max_length=300, null=True)),
                ('price', models.FloatField(max_length=5)),
                ('author', models.ManyToManyField(to='bookmanager.author')),
                ('publisher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookmanager.publisher')),
            ],
        ),
    ]
