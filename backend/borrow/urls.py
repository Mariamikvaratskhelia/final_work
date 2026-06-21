from rest_framework.routers import DefaultRouter
from .views import BorrowRecordViewSet

router = DefaultRouter()

router.register(
    'borrows',
    BorrowRecordViewSet
)

urlpatterns = router.urls