from rest_framework.test import APITestCase, APIClient
from django.urls import reverse
from article.models import Article, TimeTable, UserTimeMatchTable, SubjectTag
from dotenv import load_dotenv
import json, os

load_dotenv()

class TestViews(APITestCase):
    
    def testArticleList_normal_GET(self):
        client = APIClient()
        client.login(username='admin', password=os.environ.get('PASSWORD'))