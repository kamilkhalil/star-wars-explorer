import petl
from django.shortcuts import render, get_object_or_404, redirect
from django.core.files.base import ContentFile, File

from .utils import fetch_collection, get_file_path, DELIMITER
from .models import Collection


def index(request):
    if request.method == "POST":
        print(request.POST)
        fetch_collection()
        return redirect("index")
    elif request.method == "GET":
        char_collections = Collection.objects.order_by("-date")
        return render(request, "swapi_collections/index.html", {"collections": char_collections})


def collection_detail(request, collection_id): #TODO: validation of parameters
    collection = get_object_or_404(Collection, pk=collection_id)
    table = petl.fromcsv(get_file_path(collection.filename.name), delimiter=DELIMITER)
    headers = petl.header(table)

    if request.method == 'GET':
        if request.GET.get('filter'):
            table = petl.valuecounts(table, *request.GET.getlist('filter'))
        if request.GET.get('load_button') == 'Load More':
            elem_num = int(request.GET.get('rows_count',  0)) + 11
        else:
            elem_num = 11
            if 'frequency' in petl.header(table):
                table = petl.cut(table, *range(0, 3))
        rows = list(dict(zip(petl.header(table), x)) for x in table[1:elem_num])
        return render(request, 'swapi_collections/collection.html', {'file_name': collection.filename, 'rows': rows, 'headers': headers})



