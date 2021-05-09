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


def collection_detail(request, id): #TODO: validation of get parameters
    collection = get_object_or_404(Collection, pk=id)
    print(request.POST)
    if request.GET.get("load_button") == "Load More":
        elem_num = int(request.GET.get("rows_count",  0)) + 11
    else:
        elem_num = 11
    table = petl.fromcsv(get_file_path(collection.filename.name))
    rows = list(dict(zip(petl.header(table), x)) for x in table[1:elem_num])
    return render(request, "swapi_collections/collection.html", {"file_name": collection.filename, "rows": rows})
