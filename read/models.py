from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class WorkFile(models.Model):
	file = models.FileField(upload_to = 'excel_file/')