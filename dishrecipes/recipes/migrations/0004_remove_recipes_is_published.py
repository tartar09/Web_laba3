# Generated by Django 4.2.1 on 2024-03-14 04:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_alter_recipes_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipes',
            name='is_published',
        ),
    ]
