from django.db import models


class City(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    state = models.ForeignKey('State', on_delete=models.SET_NULL, null=True)
    search_tag = models.CharField(max_length=1000, null=True)
    status = models.DecimalField(max_digits=1, decimal_places=0)
    creation_date = models.DateTimeField(auto_now_add=True)
    creation_by = models.CharField(max_length=30)
    updation_date = models.DateTimeField(auto_now_add=True, null=True)
    updation_by = models.CharField(max_length=30, null=True)

    def __str__(self):
        return self.name
