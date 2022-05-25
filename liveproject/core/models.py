from django.db import models
from django.contrib.auth.models import User

class CustomUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    test_firstname = models.CharField(max_length=200, null=False)
    test_last_name = models.CharField(max_length=200, null=False)
    test_customemail = models.EmailField(max_length=254)


class Vacation(models.Model):
    employee = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    vaca_startdate = models.DateField()
    vaca_enddate = models.DateField()
    status = models.BooleanField()
