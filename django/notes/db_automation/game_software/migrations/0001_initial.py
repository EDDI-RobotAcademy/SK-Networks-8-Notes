# Generated by Django 5.1.3 on 2024-12-18 01:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="GameSoftware",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("title", models.CharField(max_length=32)),
            ],
            options={
                "db_table": "game_software",
            },
        ),
        migrations.CreateModel(
            name="GameSoftwareImage",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("image", models.CharField(max_length=100, null=True)),
                (
                    "gameSoftware",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="images",
                        to="game_software.gamesoftware",
                    ),
                ),
            ],
            options={
                "db_table": "game_software_image",
            },
        ),
        migrations.CreateModel(
            name="GameSoftwarePrice",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("price", models.IntegerField()),
                (
                    "gameSoftware",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="prices",
                        to="game_software.gamesoftware",
                    ),
                ),
            ],
            options={
                "db_table": "game_software_price",
            },
        ),
    ]