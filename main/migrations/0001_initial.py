# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-25 10:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Название')),
                ('slug', models.SlugField(max_length=200, unique=True)),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Название')),
                ('description', models.CharField(blank=True, max_length=100, verbose_name='Описание')),
                ('img', models.ImageField(upload_to='product_images/', verbose_name='Картинка')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена')),
                ('original_price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Оригинальная Цена')),
                ('available', models.BooleanField(default=True, verbose_name='Доступен')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='ShopAdress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adress', models.CharField(max_length=300, verbose_name='Адрес')),
                ('is_active', models.BooleanField(default=True, verbose_name='Доступен')),
            ],
            options={
                'verbose_name': 'Адрес магазина',
                'verbose_name_plural': 'Адреса магазинов',
            },
        ),
        migrations.CreateModel(
            name='ShopNumber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=300, verbose_name='Номер телефона')),
                ('is_active', models.BooleanField(default=True, verbose_name='Доступен')),
            ],
            options={
                'verbose_name': 'Номер телефона',
                'verbose_name_plural': 'Номера телефона',
            },
        ),
    ]