# Generated by Django 4.2.2 on 2023-10-18 11:18

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Test",
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
                ("ad", models.CharField(max_length=50)),
                ("category", models.CharField(max_length=50)),
                ("basliq", models.CharField(max_length=50)),
                ("metn", models.CharField(max_length=50)),
                ("img", models.FileField(upload_to="images")),
            ],
        ),
    ]
