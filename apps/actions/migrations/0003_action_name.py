# Generated by Django 5.1.3 on 2024-11-28 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actions', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='action',
            name='name',
            field=models.CharField(default='test', max_length=100),
            preserve_default=False,
        ),
    ]