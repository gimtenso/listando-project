from django.test import SimpleTestCase
from django.urls import reverse, resolve
from main.views import homepage, register_request

class TestURLS(SimpleTestCase):


    def test_register_request(self):
        url = reverse('register')
        self.assertEquals(resolve(url).func,register_request)
    

    def test_homepage_url_is_resolved(self):
        url = reverse('homepage')
        self.assertEquals(resolve(url).func, homepage)
