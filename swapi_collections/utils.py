import os
import requests
import uuid
from datetime import datetime

import petl
from django.utils import timezone
from requests.models import Response

from .models import Collection
from star_wars_explorer.settings import COLLECTIONS_PATH


FIELDS_TO_READ = [
    "name",
    "height",
    "mass",
    "hair_color",
    "eye_color",
    "skin_color",
    "birth_year",
    "gender",
    "homeworld",
    "edited",
]
DELIMITER = "\t"
homeworld_url_to_name = {}  # TODO: Better cache mechanism
SWAPI_URL = "https://swapi.dev/api/people"


def get_file_path(file_name):
    return os.path.join(COLLECTIONS_PATH, file_name)


def get_name_from_url(url: str):
    if homeworld_url_to_name.get(url) is not None:
        return homeworld_url_to_name[url]
    response = requests.get(url)
    if response.status_code == 200:
        response = response.json()
        homeworld_url_to_name[url] = response["name"]
        return response["name"]


# TODO: Data validation and error handling
def transform_response_data(response: Response):
    table = petl.fromdicts(response.json()["results"])
    table = table.cut(FIELDS_TO_READ)
    table = table.rename("edited", "date")
    date_regex = "%Y-%m-%dT%H:%M:%S.%fZ"
    table = table.convert(
        "date", lambda x: datetime.strptime(x, date_regex).strftime("%Y-%m-%d")
    )
    table = table.convert("homeworld", get_name_from_url)
    return table


def prepare_collection(date: timezone, filename: str):
    collection = Collection()
    collection.date = date
    collection.filename.name = filename
    return collection


def fetch_collection():
    response = requests.get(SWAPI_URL)
    filename = f"{uuid.uuid4().hex}.csv"
    if response.status_code == 200:
        collection = prepare_collection(timezone.now(), filename)
        table = transform_response_data(response)
        file_path = f"{COLLECTIONS_PATH}/{filename}"
        table.tocsv(file_path, delimiter=DELIMITER)
        collection.save()
        while response.status_code == 200 and response.json().get("next") is not None:
            response = requests.get(response.json()["next"])
            table = transform_response_data(response)
            table.appendcsv(file_path, delimiter=DELIMITER)
