from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User


class TestLogin(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')

    def test_login(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
