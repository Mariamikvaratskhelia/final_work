from rest_framework.viewsets import ModelViewSet
from .models import BorrowRecord
from .serializers import BorrowRecordSerializer
from rest_framework.permissions import IsAuthenticated

class BorrowRecordViewSet(ModelViewSet):

    permission_classes = [
        IsAuthenticated
    ]

    serializer_class = BorrowRecordSerializer
    queryset = BorrowRecord.objects.all()

    def get_queryset(self):
        return BorrowRecord.objects.filter(
            user=self.request.user
        )

    def perform_create(self, serializer):
        serializer.save(
            user=self.request.user
        )
