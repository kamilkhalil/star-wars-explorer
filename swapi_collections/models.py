from django.db import models

# Create your models here.

class Collection(models.Model):
    date = models.DateTimeField()
    file_path = models.FileField(upload_to='collections/')
