# Generated by Django 4.1 on 2022-09-13 21:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('media_app', '0001_initial'),
        ('category_app', '0001_initial'),
        ('catalog_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='file',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='media_app.mediafile'),
        ),
        migrations.AddField(
            model_name='post',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='category_app.tag', verbose_name='Tags'),
        ),
    ]
