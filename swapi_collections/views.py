import petl
from django.shortcuts import render, get_object_or_404
from django.core.files.base import ContentFile, File

from .utils import fetch_collection, get_file_path
from .models import Collection


def index(request):
    if request.method == "POST":
        fetch_collection()
    char_collections = Collection.objects.order_by("-date")
    return render(request, "swapi_collections/index.html", {"collections": char_collections})


def collection_detail(request, id):
    collection = get_object_or_404(Collection, pk=id)
    table = petl.fromcsv(collection.file_path)
    return render(request, "swapi_collections/collection.html", {"file_name": collection.file_path, "collection": table.data()})
