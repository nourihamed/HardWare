# Generated by Django 5.0.6 on 2024-07-23 06:04

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Equipment", "0007_remove_hardequipment_hardsupportco_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="supportcompany",
            name="companyCEOName",
            field=models.CharField(blank=True, max_length=100),
        ),
    ]