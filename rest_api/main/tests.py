from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase
from .models import Product


class ProductTest(APITestCase):

    def setUp(self):
        self.product_url = reverse('product')

    def test_get_product(self):
        self.response = self.client.get(self.product_url)
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)
