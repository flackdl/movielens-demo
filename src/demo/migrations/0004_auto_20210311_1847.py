# Generated by Django 3.1.7 on 2021-03-11 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0003_movie_movie_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='movie',
            name='tags',
            field=models.ManyToManyField(to='demo.Tag'),
        ),
    ]