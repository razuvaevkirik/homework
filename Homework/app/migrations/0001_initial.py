# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-13 09:56
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Computer',
            fields=[
                ('id_computer', models.AutoField(primary_key=True, serialize=False)),
                ('name_computer', models.CharField(max_length=100, verbose_name='Компьютер')),
                ('model_computer', models.CharField(max_length=100, verbose_name='Модель')),
                ('company_computer', models.CharField(max_length=100, verbose_name='Производитель')),
                ('price_computer', models.CharField(max_length=100, verbose_name='Цена')),
                ('characteristics_computer', models.TextField(verbose_name='Характеристики')),
                ('photo_computer', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Фото')),
            ],
            options={
                'verbose_name': 'Компьютер',
                'verbose_name_plural': 'Компьютеры',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id_order', models.AutoField(primary_key=True, serialize=False)),
                ('id_comp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Computer', verbose_name='Компьютер')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login_user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
