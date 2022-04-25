from django.db import models
from django.core.validators import RegexValidator


# Create your models here.

class ExpiryDate(models.Model):
    date = models.DateField()

    def __str__(self):
        return f"{self.date}"

class Strike(models.Model):
    strike = models.IntegerField()
    date = models.ForeignKey(ExpiryDate, on_delete=models.CASCADE,related_name='date_strike')
    def __str__(self):
        return f"{self.strike}"
