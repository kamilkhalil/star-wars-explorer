from django.db import models

from star_wars_explorer.settings import COLLECTIONS


class Collection(models.Model):
    date = models.DateTimeField()
    filename = models.FileField(upload_to=f'{COLLECTIONS}/')
