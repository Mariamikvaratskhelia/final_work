from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from books.models import Author, Book
from rest_framework import status


class BorrowProtectedTest(APITestCase):

    def setUp(self):

        self.user = User.objects.create_user(
            username='mariam',
            password='Password123'
        )

        self.author = Author.objects.create(
            name='Test Author'
        )

        self.book = Book.objects.create(
            title='Test Book',
            author=self.author
        )

    def test_unauthorized_access(self):

        response = self.client.get(
            '/api/borrows/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_401_UNAUTHORIZED
        )