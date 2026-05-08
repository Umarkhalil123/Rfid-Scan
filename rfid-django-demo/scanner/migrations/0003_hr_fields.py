from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("scanner", "0002_cardowner"),
    ]

    operations = [
        migrations.AddField(
            model_name="cardowner",
            name="department",
            field=models.CharField(blank=True, max_length=120),
        ),
        migrations.AddField(
            model_name="cardowner",
            name="employee_id",
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name="cardowner",
            name="employee_name",
            field=models.CharField(blank=True, max_length=120),
        ),
        migrations.RemoveField(
            model_name="cardowner",
            name="holder_name",
        ),
        migrations.AddField(
            model_name="scanrecord",
            name="department",
            field=models.CharField(blank=True, max_length=120),
        ),
        migrations.AddField(
            model_name="scanrecord",
            name="employee_id",
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name="scanrecord",
            name="employee_name",
            field=models.CharField(blank=True, max_length=120),
        ),
        migrations.AddField(
            model_name="scanrecord",
            name="time_in",
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="scanrecord",
            name="time_out",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.RemoveField(
            model_name="scanrecord",
            name="holder_name",
        ),
        migrations.RemoveField(
            model_name="scanrecord",
            name="scanned_at",
        ),
    ]
