# Generated by Django 5.1.2 on 2024-11-24 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0002_preferencias_alter_usuario_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='preferencias',
            name='onivoro',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='preferencias',
            name='vegetariano',
            field=models.BooleanField(default=False),
        ),
    ]
