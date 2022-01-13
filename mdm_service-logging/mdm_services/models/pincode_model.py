from django.db import models


class Pincode(models.Model):
    id = models.BigAutoField(primary_key=True)
    value = models.CharField(max_length=50)
    city = models.ForeignKey("City", on_delete=models.SET_NULL, null=True)
    serviceable = models.DecimalField(max_digits=1, decimal_places=0)
    status = models.DecimalField(max_digits=1, decimal_places=0)
    creation_date = models.DateTimeField(auto_now_add=True)
    creation_by = models.CharField(max_length=30)
    updation_date = models.DateTimeField(auto_now_add=True, null=True)
    updation_by = models.CharField(max_length=30, null=True)

    def __str__(self):
        return self.value

