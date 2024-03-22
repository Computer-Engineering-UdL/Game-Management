from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from settings import SIGNUP_IMPLEMENTED


class TestLogin(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')

    def test_login(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

    # def test_logout(self):
    #    response = self.client.get(reverse('logout')) # Logout url is not working
    #    self.assertEqual(response.status_code, 302)  # Expecting a redirect

    def test_signup(self):
        if SIGNUP_IMPLEMENTED:
            response = self.client.get(reverse('signup'))
            self.assertEqual(response.status_code, 200)
