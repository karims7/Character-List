# Generated by Django 4.0.6 on 2022-07-24 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='year_created',
            field=models.IntegerField(default=0),
        ),
    ]