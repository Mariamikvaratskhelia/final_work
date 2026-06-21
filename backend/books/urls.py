from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()

router.register(
    'authors',
    AuthorViewSet
)

router.register(
    'categories',
    CategoryViewSet
)

router.register(
    'books',
    BookViewSet
)

urlpatterns = router.urls

