from django.test import TestCase, Client
from django.urls import reverse


class URLTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_get_login(self):
        response = self.client.get(reverse('main:login'))
        self.assertEqual(response.status_code, 200)

    def test_get_register(self):
        response = self.client.get(reverse('main:register'))
        self.assertEqual(response.status_code, 200)

    def test_get_homepage(self):
        response = self.client.get(reverse('main:homepage'))
        self.assertEqual(response.status_code, 200)

    def test_get_logout(self):
        response = self.client.get(reverse('main:logout'))
        self.assertEqual(response.status_code, 302)

    def test_get_sucesso(self):
        response = self.client.get(reverse('main:sucesso'))
        self.assertEqual(response.status_code, 200)
