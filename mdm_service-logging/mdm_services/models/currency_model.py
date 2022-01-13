from django.db import models


class Currency(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    short_name = models.CharField(max_length=30)
    symbol = models.CharField(max_length=50)
    status = models.DecimalField(max_digits=1, decimal_places=0)
    creation_date = models.DateTimeField(auto_now_add=True)
    creation_by = models.CharField(max_length=30)
    updation_date = models.DateTimeField(auto_now_add=True, null=True)
    updation_by = models.CharField(max_length=30, null=True)
