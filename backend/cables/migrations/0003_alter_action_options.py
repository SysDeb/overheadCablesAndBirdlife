# Generated by Django 4.0.3 on 2022-03-25 09:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("cables", "0002_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="action",
            options={"ordering": ["-date"]},
        ),
    ]
