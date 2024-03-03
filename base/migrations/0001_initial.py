# Generated by Django 4.2.10 on 2024-02-12 18:12

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Cadastro",
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
                ("nome", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=100)),
                ("senha", models.CharField(max_length=50)),
                ("data", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
