from django.test import TestCase
from books.models import Author


class AuthorModelTest(TestCase):

    def test_author_creation(self):
        author = Author.objects.create(
            name="J.K. Rowling"
        )

        self.assertEqual(
            author.name,
            "J.K. Rowling"
        )

from rest_framework.test import APITestCase
from rest_framework import status


class BooksApiTest(APITestCase):

    def test_get_books(self):

        response = self.client.get(
            '/api/books/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )