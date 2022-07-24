# Generated by Django 4.0.6 on 2022-07-24 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('media_name', models.CharField(max_length=100)),
                ('movie_format', models.BooleanField(default=False)),
                ('description', models.TextField(max_length=500)),
                ('role', models.CharField(max_length=100)),
                ('goal', models.CharField(max_length=100)),
                ('obstacle', models.CharField(max_length=100)),
            ],
        ),
    ]
