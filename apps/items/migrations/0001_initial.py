# Generated by Django 5.1.3 on 2024-11-28 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('item_type', models.CharField(choices=[('weapon', 'Weapon'), ('armor', 'Armor'), ('helmet', 'Helmet'), ('boots', 'Boots'), ('ring', 'Ring'), ('accessory', 'Accessory'), ('misc', 'Miscellaneous')], max_length=50)),
                ('base_value', models.PositiveIntegerField(default=0)),
                ('rarity', models.CharField(choices=[('common', 'Common'), ('rare', 'Rare'), ('epic', 'Epic'), ('legendary', 'Legendary')], max_length=50)),
                ('equippable', models.BooleanField(default=False)),
            ],
        ),
    ]