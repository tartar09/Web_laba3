# Generated by Django 4.2.1 on 2024-03-14 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0004_remove_recipes_is_published'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipes',
            name='is_published',
            field=models.BooleanField(choices=[(0, 'Черновик'), (1, 'Опубликовано')], default=0),
        ),
    ]
