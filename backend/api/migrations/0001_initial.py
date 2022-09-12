# Generated by Django 4.1.1 on 2022-09-12 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="SkillTag",
            fields=[
                (
                    "name",
                    models.CharField(max_length=20, primary_key=True, serialize=False),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Application",
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
                ("name", models.CharField(max_length=150)),
                ("email", models.EmailField(max_length=254, null=True, unique=True)),
                ("selected", models.BooleanField(default=False)),
                ("collegeName", models.CharField(max_length=300)),
                (
                    "skills",
                    models.ManyToManyField(
                        blank=True, related_name="personal_skills", to="api.skilltag"
                    ),
                ),
            ],
        ),
    ]
