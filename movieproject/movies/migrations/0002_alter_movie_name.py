# Generated by Django 5.0.1 on 2024-02-08 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='name',
            field=models.TextField(max_length=20),
        ),
    ]
