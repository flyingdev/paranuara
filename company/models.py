from django.db import models


# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=1024, null=False, verbose_name='company')
