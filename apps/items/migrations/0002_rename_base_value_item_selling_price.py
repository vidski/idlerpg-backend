# Generated by Django 5.1.3 on 2024-12-04 00:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='base_value',
            new_name='selling_price',
        ),
    ]
