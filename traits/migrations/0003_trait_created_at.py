# Generated by Django 4.1.3 on 2022-11-30 14:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("traits", "0002_trait_pets"),
    ]

    operations = [
        migrations.AddField(
            model_name="trait",
            name="created_at",
            field=models.DateField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
    ]