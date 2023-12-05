from django.db import models

# Create your models here.
class Data(models.Model):
    title=models.TextField()
    year=models.TextField()
    url=models.TextField()

class DataUpdated(models.Model):
    title=models.TextField()
    year=models.TextField()
    abstract=models.TextField()
    url=models.TextField()