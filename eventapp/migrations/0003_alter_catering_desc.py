# Generated by Django 4.2.8 on 2024-01-02 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("eventapp", "0002_catering_amount_decoration_amount_photoshoot_amount"),
    ]

    operations = [
        migrations.AlterField(
            model_name="catering",
            name="desc",
            field=models.CharField(max_length=500),
        ),
    ]
