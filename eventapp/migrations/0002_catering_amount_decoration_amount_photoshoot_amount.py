# Generated by Django 4.2.8 on 2023-12-29 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("eventapp", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="catering",
            name="amount",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="decoration",
            name="amount",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="photoshoot",
            name="amount",
            field=models.IntegerField(default=0),
        ),
    ]