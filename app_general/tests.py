from django.test import TestCase

# Create your tests here.
from django.test import Client
# create an instance of the client for our use
client = Client()

class App_General_Test(TestCase):

    def test_default_page(self):
        response = client.get('/')        
        #self.assertIs(future_question.was_published_recently(), False)
        self.assertEqual(response.status_code, 200)
