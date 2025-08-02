#localhost:8000/myapp/students=>All Crud operatons
from .models import Users
from .serializer import UsersSerializer
from rest_framework import viewsets
class UsersViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer


