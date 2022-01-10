# Generated by Django 4.0.1 on 2022-01-10 12:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("sinp_nomenclatures", "0002_alter_source_unique_together"),
        ("cables", "0011_alter_segment_building_integration_risk_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="pole",
            name="attraction_advice",
            field=models.BooleanField(
                default=False, verbose_name="Attraction"
            ),
        ),
        migrations.AddField(
            model_name="pole",
            name="dissuasion_advice",
            field=models.BooleanField(
                default=False, verbose_name="Dissuasion"
            ),
        ),
        migrations.AddField(
            model_name="pole",
            name="isolation_advice",
            field=models.BooleanField(default=False, verbose_name="Isolation"),
        ),
        migrations.AddField(
            model_name="pole",
            name="pole_attractivity",
            field=models.ForeignKey(
                help_text="Level of risk",
                limit_choices_to={"type__mnemonic": "risk_level"},
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="+",
                to="sinp_nomenclatures.item",
                verbose_name="Level of risk",
            ),
        ),
        migrations.AddField(
            model_name="pole",
            name="pole_dangerousness",
            field=models.ForeignKey(
                help_text="Level of risk",
                limit_choices_to={"type__mnemonic": "risk_level"},
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="+",
                to="sinp_nomenclatures.item",
                verbose_name="Level of risk",
            ),
        ),
        migrations.AddField(
            model_name="pole",
            name="pole_type_primary",
            field=models.ForeignKey(
                help_text="Pole type",
                limit_choices_to={"type__mnemonic": "pole_type"},
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="+",
                to="sinp_nomenclatures.item",
                verbose_name="Pole type",
            ),
        ),
        migrations.AddField(
            model_name="pole",
            name="pole_type_secondary",
            field=models.ForeignKey(
                help_text="Pole type",
                limit_choices_to={"type__mnemonic": "pole_type"},
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="+",
                to="sinp_nomenclatures.item",
                verbose_name="Pole type",
            ),
        ),
    ]
