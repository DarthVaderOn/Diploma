# Generated by Django 4.1 on 2022-09-29 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog_app', '0006_alter_media_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='price',
            field=models.PositiveIntegerField(blank=True, default=0, help_text='Indicate the amount in Belarusian rubles', verbose_name='Price'),
        ),
    ]