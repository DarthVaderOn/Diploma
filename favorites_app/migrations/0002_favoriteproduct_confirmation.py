# Generated by Django 4.1 on 2022-09-15 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('favorites_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='favoriteproduct',
            name='confirmation',
            field=models.BooleanField(default=False),
        ),
    ]
