from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from django.urls import reverse
from article.models import *
from dotenv import load_dotenv
import json, os

load_dotenv()

class testArticleList(APITestCase):
    def setUp(self):
        self.url = reverse('list')
    
    def test_GET_articlelist_success(self):
        response = self.client.get(self.url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)