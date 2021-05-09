from django.test import TestCase, Client
from django.urls import reverse
from django.utils import timezone


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
    
    def test_home_page(self):
        response = self.client.get('http://127.0.0.1:8000')
        self.assertEqual(response.status_code, 200)

    