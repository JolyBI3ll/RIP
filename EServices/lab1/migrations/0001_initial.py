# Generated by Django 4.2.4 on 2023-09-26 15:57

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Moderator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Имя')),
                ('login', models.CharField(max_length=20, verbose_name='Логин')),
                ('password', models.CharField(max_length=50, verbose_name='Пароль')),
            ],
        ),
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=50, verbose_name='ФИО')),
                ('link', models.CharField(blank=True, max_length=50, null=True, verbose_name='Ссылка на изображение')),
                ('status', models.CharField(max_length=1, verbose_name='Статус активности')),
                ('bdate', models.DateField(verbose_name='День рождения')),
                ('sport', models.CharField(max_length=20, verbose_name='Тип занятия')),
                ('description', models.CharField(blank=True, max_length=255, null=True, verbose_name='Описание')),
                ('power', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)], verbose_name='Сила')),
                ('agility', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)], verbose_name='Ловкость')),
                ('endurance', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)], verbose_name='Выносливость')),
                ('last_modified', models.DateTimeField(auto_now=True, null=True, verbose_name='Последнее изменение')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Имя')),
                ('login', models.CharField(max_length=20, verbose_name='Логин')),
                ('password', models.CharField(max_length=50, verbose_name='Пароль')),
            ],
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now=True, verbose_name='Создание')),
                ('send', models.DateTimeField(verbose_name='Отправка')),
                ('closed', models.DateTimeField(verbose_name='Закрытие')),
                ('status', models.CharField(max_length=20, verbose_name='Статус')),
                ('moderator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lab1.moderator', verbose_name='Модератор')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lab1.user', verbose_name='Пользователь')),
            ],
        ),
        migrations.CreateModel(
            name='OrdersProducts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lab1.participant', verbose_name='Участник')),
                ('Request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lab1.request', verbose_name='Заявка')),
            ],
        ),
    ]
