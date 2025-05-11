import unittest
from typing import Optional, Any
from io import BytesIO
from view import HttpRequest, HttpResponse, my_view, AnonymousUser, User

class TestMyView(unittest.TestCase):

    def test_anonymous_user(self):
        request = HttpRequest(AnonymousUser(id=1, username="hi",pk=1,is_staff=False,is_active=True,is_superuser=True), "Hello")
        response = my_view(request)
        assert response.id == None

    def test_authenticated_user(self):
        request = HttpRequest(User(id=42, username="hi",pk=1,is_staff=False,is_active=True,is_superuser=True), "Hello")
        response = my_view(request)

        assert response.id == 43

if __name__ == '__main__':
    unittest.main()