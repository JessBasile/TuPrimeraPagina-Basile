# Generated by Django 5.1.6 on 2025-03-05 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='infoextra',
            name='asignatura',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
