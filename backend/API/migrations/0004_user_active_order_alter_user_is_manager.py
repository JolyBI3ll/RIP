# Generated by Django 4.2.6 on 2023-10-10 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_request_closed_alter_request_send'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='active_order',
            field=models.IntegerField(default=-1, verbose_name='Активный заказ'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_manager',
            field=models.BooleanField(verbose_name='Модератор?'),
        ),
    ]