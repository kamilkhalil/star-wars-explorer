import os
from django.conf import settings
from django.core.files.storage import FileSystemStorage


class ExistingFileStorage(FileSystemStorage):
    def get_available_name(self, name):
        if self.exists(name):
            os.remove(os.path.join(settings.MEDIA_ROOT, name))
        return name 