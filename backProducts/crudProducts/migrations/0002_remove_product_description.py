# Generated by Django 5.2 on 2025-04-18 15:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crudProducts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='description',
        ),
    ]
