# Generated by Django 4.2 on 2023-04-24 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("functionality", "0005_alter_activity_user_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="activity", name="date_time_added", field=models.DateTimeField(),
        ),
    ]