from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("scanner", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="CardOwner",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("card_uid", models.CharField(max_length=100, unique=True)),
                ("holder_name", models.CharField(max_length=120)),
            ],
        ),
    ]
