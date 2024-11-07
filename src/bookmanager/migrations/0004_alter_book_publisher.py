# Generated by Django 5.1.2 on 2024-10-31 13:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookmanager', '0003_alter_book_publisher'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookmanager.publisher'),
        ),
    ]
