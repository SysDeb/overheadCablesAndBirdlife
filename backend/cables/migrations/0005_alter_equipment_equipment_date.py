# Generated by Django 4.0.1 on 2022-01-18 08:35

import datetime

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cables", "0004_alter_equipment_equipment_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="equipment",
            name="equipment_date",
            field=models.DateTimeField(
                default=datetime.datetime(2022, 1, 18, 9, 35, 54, 569285),
                editable=False,
            ),
        ),
    ]
