# Generated by Django 4.2 on 2023-05-02 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("functionality", "0007_remove_activity_date_time_finish"),
    ]

    operations = [
        migrations.RemoveField(model_name="activity", name="completed",),
        migrations.AddField(
            model_name="activity",
            name="completion",
            field=models.DecimalField(decimal_places=3, default=0, max_digits=4),
        ),
        migrations.AddField(
            model_name="activity",
            name="duration",
            field=models.IntegerField(default=1),
        ),
    ]