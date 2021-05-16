from django.test import SimpleTestCase
from django.urls import reverse, resolve
from swapi_collections.views import index, collection_detail


class TestUrls(SimpleTestCase):

    def test_index_url_resolves(self):
        url = reverse('index')
        self.assertEqual(resolve(url).func, index)

    def test_collection_detail_url_resolves(self):
        url = reverse('detail', kwargs={'collection_id': 1})
        self.assertEqual(resolve(url).func, collection_detail)