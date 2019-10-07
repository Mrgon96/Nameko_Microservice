from django.db import models

# Create your models here.


class Students(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    roll = models.IntegerField(null=False, blank=False)
