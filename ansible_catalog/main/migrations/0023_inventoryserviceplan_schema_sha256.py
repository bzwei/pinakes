# Generated by Django 3.2.5 on 2021-12-14 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0022_auto_20211214_1835"),
    ]

    operations = [
        migrations.AddField(
            model_name="inventoryserviceplan",
            name="schema_sha256",
            field=models.TextField(blank=True, default=""),
        ),
    ]