# Generated by Django 4.1 on 2023-01-10 02:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mensajes', '0002_alter_mensajes_mensaje_alter_mensajes_tiempo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mensajes',
            old_name='recibir',
            new_name='destinatario',
        ),
        migrations.RenameField(
            model_name='mensajes',
            old_name='enviar',
            new_name='enviar_a',
        ),
        migrations.RenameField(
            model_name='mensajes',
            old_name='tiempo',
            new_name='fecha',
        ),
    ]
