# Generated by Django 4.1 on 2022-08-19 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Response",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("deleted", models.BooleanField(blank=True, default=False)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("identifier", models.TextField()),
                ("values", models.TextField()),
                ("discord_guild", models.TextField()),
                ("discord_author", models.TextField()),
                ("discord_channel", models.TextField()),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
