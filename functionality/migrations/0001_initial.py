# Generated by Django 4.2 on 2023-04-17 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Activity",
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
                ("activity_name", models.CharField(max_length=200)),
                ("date_time_start", models.DateTimeField()),
                ("date_time_finish", models.DateTimeField()),
                ("date_time_added", models.DateTimeField()),
                ("record_description", models.CharField(max_length=2000)),
            ],
        ),
    ]
