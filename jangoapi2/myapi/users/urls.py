from django.urls import path,include
from .views import UsersViewSet
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register(f"users",UsersViewSet)
urlpatterns = [
    path('',include(router.urls))
]