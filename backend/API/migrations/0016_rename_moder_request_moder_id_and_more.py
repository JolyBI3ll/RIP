# Generated by Django 4.2.6 on 2023-11-20 16:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_rename_moder_id_request_moder_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='request',
            old_name='moder',
            new_name='moder_id',
        ),
        migrations.RenameField(
            model_name='request',
            old_name='user',
            new_name='user_id',
        ),
    ]