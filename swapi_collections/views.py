import requests
import uuid
import petl as etl
import os
from datetime import datetime
from django.shortcuts import render
from django.core.files.base import ContentFile, File

from .models import Collection
from star_wars_explorer.settings import MEDIA_ROOT

FIELDS_TO_READ = ['name', 'height', 'mass', 'hair_color', "skin_color", "eye_color", "birth_year", "gender", "homeworld", "edited"]
date_regex = "%Y-%m-%dT%H:%M:%S.%fZ"
output_date_regex = "%Y-%m-%d"
#datetime.strptime('2014-12-20T21:17:56.891000Z', "%Y-%m-%dT%H:%M:%S.%fZ")
COLLECTIONS_PATH = os.path.join(MEDIA_ROOT, 'collections')


homeworld_url_to_name = {}


def get_name_from_url(url):
    if homeworld_url_to_name.get(url) is not None:
        return homeworld_url_to_name[url]
    response = requests.get(url)
    if response.status_code == 200:
        response = response.json()
        homeworld_url_to_name[url] = response["name"] 
        return response["name"]


def transform_response_data(data):
    table = etl.fromdicts(data.json()["results"])
    table = table.cut(FIELDS_TO_READ)
    table = table.rename("edited", "date")
    table = table.convert('date', lambda x: datetime.strptime(x, date_regex).strftime("%Y-%m-%d"))
    table = table.convert('homeworld', get_name_from_url)
    return table


def prepare_collection(date, file_name):
    collection = Collection()
    collection.date = date
    collection.file_path.name = file_name
    return collection


def fetch_collection():
        response = requests.get("https://swapi.dev/api/people")
        date = datetime.now()
        file_name = f"{uuid.uuid4().hex}.csv"
        file_path = f'{COLLECTIONS_PATH}/{file_name}'
        if response.status_code == 200:
            collection = prepare_collection(date, file_name)
            table = transform_response_data(response)
            table.tocsv(file_path, delimiter="|")
            collection.save()
            while response.status_code == 200 and response.json().get("next") is not None:
                response = requests.get(response.json()["next"])
                table =  transform_response_data(response)
                table.appendcsv(file_path, delimiter="|")


def index(request):
    if request.method == "POST":
        fetch_collection()
    return render(request, "swapi_collections/index.html")
