# Generated by Django 4.1.1 on 2022-09-12 20:32

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0002_alter_application_skills"),
    ]

    operations = [
        migrations.AlterField(
            model_name="application",
            name="id",
            field=models.UUIDField(
                default=uuid.uuid4,
                editable=False,
                primary_key=True,
                serialize=False,
                unique=True,
            ),
        ),
    ]
