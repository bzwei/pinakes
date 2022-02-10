# Generated by Django 3.2.5 on 2022-02-04 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0033_auto_20220203_1418"),
    ]

    operations = [
        migrations.AddField(
            model_name="source",
            name="info",
            field=models.JSONField(
                blank=True,
                help_text="The information about the source",
                null=True,
            ),
        ),
    ]