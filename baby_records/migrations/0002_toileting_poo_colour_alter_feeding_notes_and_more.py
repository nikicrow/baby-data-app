# Generated by Django 4.2.2 on 2023-07-16 03:50

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baby_records', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='toileting',
            name='poo_colour',
            field=models.CharField(default='brown'),
        ),
        migrations.AlterField(
            model_name='feeding',
            name='notes',
            field=models.CharField(blank=True, default='n/a', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='toileting',
            name='notes',
            field=models.CharField(blank=True, default='n/a', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='toileting',
            name='pee_scale',
            field=models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='toileting',
            name='poo_scale',
            field=models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)]),
        ),
    ]