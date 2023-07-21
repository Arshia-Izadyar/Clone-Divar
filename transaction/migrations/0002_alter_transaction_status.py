# Generated by Django 4.2 on 2023-07-21 07:37

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("transaction", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="transaction",
            name="status",
            field=models.SmallIntegerField(
                choices=[(10, "paid"), (0, "pending"), (-10, "Not paid")],
                default=-10,
                verbose_name="Status",
            ),
        ),
    ]