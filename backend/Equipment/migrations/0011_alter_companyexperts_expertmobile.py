# Generated by Django 5.0.6 on 2024-08-03 06:38

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Equipment", "0010_subcategories_subcat_manufacture"),
    ]

    operations = [
        migrations.AlterField(
            model_name="companyexperts",
            name="expertMobile",
            field=models.CharField(max_length=13, unique=True),
        ),
    ]
