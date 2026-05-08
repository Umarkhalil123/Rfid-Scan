from django.db import models


class CardOwner(models.Model):
    card_uid = models.CharField(max_length=100, unique=True)
    employee_id = models.CharField(max_length=50, blank=True)
    employee_name = models.CharField(max_length=120, blank=True)
    department = models.CharField(max_length=120, blank=True)

    def __str__(self):
        return f"{self.card_uid} -> {self.employee_name or 'Unknown'}"


class ScanRecord(models.Model):
    card_uid = models.CharField(max_length=100)
    employee_id = models.CharField(max_length=50, blank=True)
    employee_name = models.CharField(max_length=120, blank=True)
    department = models.CharField(max_length=120, blank=True)
    time_in = models.DateTimeField()
    time_out = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.card_uid} @ {self.time_in:%Y-%m-%d %H:%M:%S}"
