# Generated by Django 4.2.20 on 2025-05-08 10:20

from decimal import Decimal

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("checkout", "0078_merge_20250507_0613"),
    ]

    operations = [
        migrations.AlterField(
            model_name="checkoutline",
            name="prior_unit_price_amount",
            field=models.DecimalField(
                blank=True, decimal_places=3, max_digits=20, null=True
            ),
        ),
        migrations.AlterField(
            model_name="checkoutline",
            name="undiscounted_unit_price_amount",
            field=models.DecimalField(
                decimal_places=3, default=Decimal(0), max_digits=20
            ),
        ),
    ]
