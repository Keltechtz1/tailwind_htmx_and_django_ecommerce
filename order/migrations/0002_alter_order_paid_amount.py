# Generated by Django 4.2.19 on 2025-02-21 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='paid_amount',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
