# Generated by Django 4.1 on 2023-01-08 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0002_alter_post_receta'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='imagenPost',
            field=models.ImageField(blank=True, upload_to='posteo'),
        ),
    ]
