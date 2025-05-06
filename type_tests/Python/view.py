from typing import Optional, Any
from io import BytesIO

class User:
    def __init__(self, id, pk, username, is_staff, is_active, is_superuser):
        self.id = id
        self.pk = pk
        self.username = username
        self.is_staff = is_staff
        self.is_active = is_active
        self.is_superuser = is_superuser

class AnonymousUser(User):
    def __init__(self, id, pk, username, is_staff, is_active, is_superuser):
        super().__init__(id, pk, username, is_staff, is_active, is_superuser)
        self.id = None
        self.username = "Anonymous User"
        self.is_staff = False
        self.is_active = False
        self.is_superuser = False
    
class HttpRequest():
    def __init__(self, user, content):
        self.user = user
        self.content = content


class HttpResponse():
    def __init__(self, id):
        self.id = id

def my_view(request: HttpRequest) -> HttpResponse:
    current_id_plus_one = request.user.id + 1
    return HttpResponse(current_id_plus_one)