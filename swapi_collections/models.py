from django.db import models

from django.core.files.storage import FileSystemStorage

from star_wars_explorer.settings import COLLECTIONS

# upload_storage = FileSystemStorage(location=MEDIA_ROOT, base_url='/')


class Collection(models.Model):
    date = models.DateTimeField()
    filename = models.FileField(upload_to=f'{COLLECTIONS}/')
