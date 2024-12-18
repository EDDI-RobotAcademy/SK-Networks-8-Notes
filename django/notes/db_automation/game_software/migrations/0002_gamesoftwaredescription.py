# Generated by Django 5.1.3 on 2024-12-18 08:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("game_software", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="GameSoftwareDescription",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("description", models.TextField()),
                (
                    "gameSoftware",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="descriptions",
                        to="game_software.gamesoftware",
                    ),
                ),
            ],
            options={
                "db_table": "game_software_description",
            },
        ),
    ]
