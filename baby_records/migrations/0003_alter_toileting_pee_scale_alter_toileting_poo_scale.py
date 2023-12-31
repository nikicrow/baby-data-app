# Generated by Django 4.2.2 on 2023-07-16 04:55

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baby_records', '0002_toileting_poo_colour_alter_feeding_notes_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='toileting',
            name='pee_scale',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='toileting',
            name='poo_scale',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(0)]),
        ),
    ]
