# Generated by Django 4.2 on 2024-05-26 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='preferred_theme',
            field=models.CharField(choices=[('Темная', 'Dark'), ('Светлая', 'Light')], default='Светлая', max_length=10),
        ),
    ]