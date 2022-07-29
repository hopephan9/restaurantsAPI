from django.test import TestCase
from rest_framework.test import APIClient
from django.apps import apps
from django.conf import settings
import django

# Create your tests here.
class RestaurantTestCase(TestCase):
    api_client = APIClient()
    django.setup()
    def test_restaurants(self):
        res = self.api_client.get("/restaurant/")
        self.assertEqual(res.status_code, 200)
        self.assertEqual(len(res.data), 29)

    def test_restaurantsfiltering(self):
        res = self.api_client.get("/restaurant/?name__icontains=casi+cielo")
        self.assertEqual(res.status_code, 200)
        self.assertEqual(len(res.data), 1)