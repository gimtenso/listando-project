from django.test import TestCase, Client
from django.urls import reverse
import json

class TesteViews(TestCase):


    def test_homepage_view(self):
        client = Client()
        response = client.get(reverse('homepage'))
        self.assertEqual(response.status_code,200)


   


    def register_request_view(self):
        client = Client()
        response = client.get(reverse('regiter'))
        self.assertEqual(response.status_code,200)

    def test_login_view(self):
        client = Client()
        response = client.get(reverse('login'))
        self.assertEqual(response.status_code,200)

    def test_logout_view(self):
        client = Client()
        response = client.get(reverse('logout'))
        self.assertEqual(response.status_code,200)


    def test_sucesso_view(self):
        client = Client()
        response = client.get(reverse('sucesso'))
        self.assertEqual(response.status_code,200)


  
