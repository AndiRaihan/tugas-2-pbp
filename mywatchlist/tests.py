from django.test import TestCase, Client
from django.urls import resolve

# Create your tests here.
class TestCaseMyWatchList(TestCase):
    def test_return_html(self):
        response = Client().get('/mywatchlist/html/')
        self.assertEqual(response.status_code, 200)
        
    def test_return_xml(self):
        response = Client().get('/mywatchlist/xml/')
        self.assertEqual(response.status_code, 200)

    def test_return_json(self):
        response = Client().get('/mywatchlist/json/')
        self.assertEqual(response.status_code, 200)
    