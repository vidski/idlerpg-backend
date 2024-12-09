# Generated by Django 5.1.3 on 2024-11-28 10:35

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('inventory', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='EquippedItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accessory', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='equipped_as_accessory', to='inventory.inventoryitem')),
                ('armor', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='equipped_as_armor', to='inventory.inventoryitem')),
                ('boots', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='equipped_as_boots', to='inventory.inventoryitem')),
                ('helmet', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='equipped_as_helmet', to='inventory.inventoryitem')),
                ('ring_left', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='equipped_as_ring_left', to='inventory.inventoryitem')),
                ('ring_right', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='equipped_as_ring_right', to='inventory.inventoryitem')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='loadout', to=settings.AUTH_USER_MODEL)),
                ('weapon', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='equipped_as_weapon', to='inventory.inventoryitem')),
            ],
        ),
    ]
