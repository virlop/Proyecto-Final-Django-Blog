# Generated by Django 4.0.4 on 2022-06-22 13:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('virginiaBlog', '0002_blogmodel_delete_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogmodel',
            name='fecha_creacion',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]