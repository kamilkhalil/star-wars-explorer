from unittest.mock import patch

from django.test import TestCase, Client
from django.urls import reverse
from django.utils import timezone

from swapi_collections.utils import FIELDS_TO_READ, prepare_collection


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.index_url = reverse("index")
        self.detail_url = reverse("detail", args=[1])
        collection1 = prepare_collection(timezone.now(), "collection.csv")
        collection1.save()

    def test_index_GET(self):
        response = self.client.get(self.index_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context["collections"]), 1)
        self.assertTemplateUsed(response, "swapi_collections/index.html")

    @patch("swapi_collections.views.fetch_collection")
    def test_index_POST(self, mock_fetch_collection):
        response = self.client.post(self.index_url)
        self.assertEqual(response.status_code, 302)

    @patch("swapi_collections.views.petl.fromcsv")
    def test_collection_detail_GET(self, mock_fromcsv):
        mock_fromcsv.return_value = [
            FIELDS_TO_READ,
            [
                "Luke Skywalker",
                "172",
                "77",
                "blond",
                "blue",
                "19BBY",
                "male",
                "Tatooine",
                "2014-12-20",
            ],
        ]
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["file_name"], "collection.csv")
        self.assertEqual(len(response.context["rows"]), 1)
        self.assertEqual(response.context["headers"], tuple(FIELDS_TO_READ))
        self.assertTemplateUsed(response, "swapi_collections/collection.html")

    @patch("swapi_collections.views.petl.fromcsv")
    def test_collection_detail_GET_load_more(self, mock_fromcsv):
        mock_fromcsv.return_value = [
            FIELDS_TO_READ,
            [
                "Luke Skywalker",
                "172",
                "77",
                "blond",
                "blue",
                "19BBY",
                "male",
                "Tatooine",
                "2014-12-20",
            ],
        ]
        response = self.client.get(self.detail_url, {"load_button": "Load More"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["file_name"], "collection.csv")
        self.assertEqual(len(response.context["rows"]), 1)
        self.assertEqual(response.context["headers"], tuple(FIELDS_TO_READ))
        self.assertTemplateUsed(response, "swapi_collections/collection.html")

    @patch("swapi_collections.views.petl.fromcsv")
    def test_collection_detail_GET_filter(self, mock_fromcsv):
        mock_fromcsv.return_value = [
            FIELDS_TO_READ,
            [
                "Luke Skywalker",
                "172",
                "77",
                "blond",
                "blue",
                "19BBY",
                "male",
                "Tatooine",
                "2014-12-20",
            ],
        ]
        filter_content = ["hair_color", "eye_color"]
        response = self.client.get(self.detail_url, {"filter": filter_content})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["file_name"], "collection.csv")
        self.assertEqual(len(response.context["rows"]), 1)
        self.assertEqual(
            list(response.context["rows"][0].keys()), filter_content + ["count"]
        )
        self.assertEqual(response.context["headers"], tuple(FIELDS_TO_READ))
        self.assertTemplateUsed(response, "swapi_collections/collection.html")

    @patch("swapi_collections.views.petl.fromcsv")
    def test_collection_detail_GET_filter_no_data(self, mock_fromcsv):
        mock_fromcsv.return_value = []
        filter_content = ["hair_color", "eye_color"]
        response = self.client.get(self.detail_url, {"filter": filter_content})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["file_name"], "collection.csv")
        self.assertEqual(len(response.context["rows"]), 0)
        self.assertEqual(response.context["headers"], [])
        self.assertTemplateUsed(response, "swapi_collections/collection.html")

    @patch("swapi_collections.views.petl.fromcsv")
    def test_collection_detail_GET_wrong_filter(self, mock_fromcsv):
        mock_fromcsv.return_value = [
            FIELDS_TO_READ,
            [
                "Luke Skywalker",
                "172",
                "77",
                "blond",
                "blue",
                "19BBY",
                "male",
                "Tatooine",
                "2014-12-20",
            ],
        ]
        filter_content = ["non_existent_field"]
        response = self.client.get(self.detail_url, {"filter": filter_content})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["file_name"], "collection.csv")
        self.assertEqual(len(response.context["rows"]), 0)
        self.assertEqual(response.context["headers"], tuple(FIELDS_TO_READ))
        self.assertTemplateUsed(response, "swapi_collections/collection.html")
