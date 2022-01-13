from django.db import models


class Institute(models.Model):
    id = models.BigAutoField(primary_key=True)
    university = models.ForeignKey("University", on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=50)
    city = models.ForeignKey("City", on_delete=models.SET_NULL, null=True)
    ranking = models.DecimalField(max_digits=5, decimal_places=0, default=1)
    ranking_source = models.CharField(max_length=120)
    serviceable = models.BooleanField(default=True)
    blacklisted = models.BooleanField(default=False)
    search_tag = models.CharField(max_length=1000, null=True)
    status = models.DecimalField(max_digits=1, decimal_places=0)
    creation_date = models.DateTimeField(auto_now_add=True)
    creation_by = models.CharField(max_length=30)
    updation_date = models.DateTimeField(auto_now_add=True, null=True)
    updation_by = models.CharField(max_length=30, null=True)

    def __str__(self):
        return self.name
