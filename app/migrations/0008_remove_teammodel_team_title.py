# Generated by Django 5.1 on 2024-08-15 14:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_teammodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teammodel',
            name='team_title',
        ),
    ]
