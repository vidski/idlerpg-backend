# Generated by Django 5.1.3 on 2024-11-28 10:35

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('actions', '0001_initial'),
        ('items', '0001_initial'),
        ('skills', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='action',
            name='skill',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='skills.skill'),
        ),
        migrations.AddField(
            model_name='actionrequirement',
            name='action',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='actions.action'),
        ),
        migrations.AddField(
            model_name='actionrequirement',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='items.item'),
        ),
        migrations.AddField(
            model_name='action',
            name='item_requirements',
            field=models.ManyToManyField(blank=True, related_name='item_requirements', through='actions.ActionRequirement', to='items.item'),
        ),
        migrations.AddField(
            model_name='actionreward',
            name='action',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='actions.action'),
        ),
        migrations.AddField(
            model_name='actionreward',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='items.item'),
        ),
        migrations.AddField(
            model_name='action',
            name='item_rewards',
            field=models.ManyToManyField(blank=True, related_name='item_rewards', through='actions.ActionReward', to='items.item'),
        ),
        migrations.AddField(
            model_name='useraction',
            name='action',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='actions.action'),
        ),
        migrations.AddField(
            model_name='useraction',
            name='skill',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='skills.skill'),
        ),
        migrations.AddField(
            model_name='useraction',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='action', to=settings.AUTH_USER_MODEL),
        ),
    ]