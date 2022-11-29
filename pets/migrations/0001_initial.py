# Generated by Django 4.1.3 on 2022-11-29 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Pet",
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
                ("name", models.CharField(max_length=50)),
                ("age", models.IntegerField()),
                ("weight", models.FloatField()),
                (
                    "sex",
                    models.CharField(
                        choices=[
                            ("Male", "Male"),
                            ("Female", "Female"),
                            ("Not_Informed", "Not Informed"),
                        ],
                        default="Not_Informed",
                        max_length=20,
                    ),
                ),
            ],
        ),
    ]
