from rest_framework.test import APITestCase
from django.contrib.auth.models import User


class RegistrationTest(APITestCase):

    def test_user_registration(self):

        data = {
            "username": "mariam",
            "email": "mariam@test.com",
            "password": "Password123"
        }

        response = self.client.post(
            '/api/register/',
            data
        )

        self.assertEqual(
            response.status_code,
            201
        )

        self.assertTrue(
            User.objects.filter(
                username="mariam"
            ).exists()
        )
class LoginTest(APITestCase):

    def setUp(self):

        User.objects.create_user(
            username='mariam',
            password='Password123'
        )

    def test_login(self):

        response = self.client.post(
            '/api/login/',
            {
                "username": "mariam",
                "password": "Password123"
            }
        )

        self.assertEqual(
            response.status_code,
            200
        )

        self.assertIn(
            'access',
            response.data
        )