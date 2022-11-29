# Generated by Django 4.1.3 on 2022-11-29 04:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("pets", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Group",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("scientific_name", models.CharField(max_length=50, unique=True)),
                ("created_at", models.DateField(auto_now=True)),
                (
                    "pet",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="groups",
                        to="pets.pet",
                    ),
                ),
            ],
        ),
    ]
