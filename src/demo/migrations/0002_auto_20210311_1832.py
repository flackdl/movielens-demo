# Generated by Django 3.1.7 on 2021-03-11 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genre',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
