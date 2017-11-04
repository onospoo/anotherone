# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-02 11:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0008_auto_20171102_1701'),
    ]

    operations = [
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя района')),
                ('delivery_price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена доставки')),
            ],
            options={
                'verbose_name': 'Район',
                'verbose_name_plural': 'Районы',
            },
        ),
        migrations.AlterField(
            model_name='order',
            name='order_status',
            field=models.CharField(choices=[('Завершен', 'Завершен'), ('Выполняется', 'Выполняется'), ('Новый', 'Новый')], default='Новый', max_length=20, verbose_name='Состояние заказа'),
        ),
        migrations.AddField(
            model_name='order',
            name='district',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='cart.District', verbose_name='Район'),
            preserve_default=False,
        ),
    ]