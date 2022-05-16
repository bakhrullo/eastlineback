from django.db import models


# Create your models here.

class UserInfo(models.Model):
    tgUserId = models.IntegerField()
    cashBack = models.IntegerField(null=True, blank=True)
    phone = models.CharField(max_length=20, unique=True)
    inVoiceId = models.CharField(max_length=20, unique=True, null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    cashBackDate = models.DateField(auto_now=True)
    name = models.CharField(max_length=1000, null=True, blank=True)

