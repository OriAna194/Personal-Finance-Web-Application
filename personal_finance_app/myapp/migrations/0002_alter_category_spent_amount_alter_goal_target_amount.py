# Generated by Django 5.0.6 on 2024-12-14 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='spent_amount',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='goal',
            name='target_amount',
            field=models.FloatField(default=0),
        ),
    ]
