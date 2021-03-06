# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-25 10:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date_order',
            field=models.DateField(blank=True, verbose_name='Дата заказа'),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_status',
            field=models.CharField(choices=[('Завершен', 'Завершен'), ('Выполняется', 'Выполняется'), ('Новый', 'Новый')], default='Новый', max_length=10, verbose_name='Состояние заказа'),
        ),
        migrations.AlterField(
            model_name='order',
            name='payment_status',
            field=models.CharField(choices=[('Карта', 'Cбербанк ОНЛАЙН'), ('Нал', 'Наличные')], max_length=30, verbose_name='Способ оплаты'),
        ),
    ]
