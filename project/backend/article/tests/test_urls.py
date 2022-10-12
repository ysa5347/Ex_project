from django.test import SimpleTestCase
from django.urls import reverse, resolve
from article.views import ArticleDelete, ArticlePtcp, ArticleUpdate, helloAPI, ArticleList, ArticleView, ArticleCreate

class TestUrls(SimpleTestCase):
    
    def test_list_url_is_resolved(self):
        url = '/article/'
        self.assertEquals(resolve(url).func, ArticleList)

    def test_view_url_is_resolved(self):
        k = 1
        url = reverse('view', args=[k])
        self.assertEquals(resolve(url).func, ArticleView)