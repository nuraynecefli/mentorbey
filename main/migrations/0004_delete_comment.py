# Generated by Django 4.2.2 on 2023-10-20 11:51

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0003_comment"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Comment",
        ),
    ]