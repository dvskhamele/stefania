from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import JSONField



# Create your models here.
class WorkFile(models.Model):

    data = JSONField(blank=True, null = True)
    mess = models.TextField(blank = True, null = True)