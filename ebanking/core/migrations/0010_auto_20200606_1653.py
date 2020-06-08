# Generated by Django 3.0.7 on 2020-06-06 16:53

import core.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20200606_1004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='account_number',
            field=models.CharField(default=core.models.generate_account_number, max_length=10, validators=[django.core.validators.validate_integer]),
        ),
        migrations.AlterField(
            model_name='application',
            name='phone',
            field=models.CharField(max_length=15, validators=[django.core.validators.validate_integer]),
        ),
        migrations.AlterField(
            model_name='application',
            name='pin',
            field=models.CharField(max_length=4, validators=[django.core.validators.validate_integer]),
        ),
        migrations.AlterField(
            model_name='beneficiary',
            name='beneficiary_account',
            field=models.CharField(max_length=15, validators=[django.core.validators.validate_integer]),
        ),
        migrations.AlterField(
            model_name='beneficiary',
            name='beneficiary_phone',
            field=models.CharField(max_length=15, validators=[django.core.validators.validate_integer]),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='phone',
            field=models.CharField(max_length=15, validators=[django.core.validators.validate_integer]),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='pin',
            field=models.CharField(max_length=4, validators=[django.core.validators.validate_integer]),
        ),
    ]
