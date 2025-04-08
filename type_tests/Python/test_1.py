import unittest
from django.http import HttpRequest, HttpResponse

class User:
    def __init__(self, id: Optional[int]):
        self.id = id

class AnonymousUser:
    id = None

class TestMyView(unittest.TestCase):

    def test_anonymous_user(self):
        # Create a request with an AnonymousUser
        request = HttpRequest()
        request.user = AnonymousUser()

        # Call the view
        response = my_view(request)

        # Check the response content is as expected (0 for anonymous user)
        self.assertEqual(response.content.decode(), '0')

    def test_authenticated_user(self):
        # Create a request with a normal user (id = 42)
        request = HttpRequest()
        request.user = User(id=42)

        # Call the view
        response = my_view(request)

        # Check the response content is the user's id + 1 (43)
        self.assertEqual(response.content.decode(), '43')

if __name__ == '__main__':
    unittest.main()