from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny

from .tasks import send_welcome_email


# -----------------------------
# REGISTER VIEW
# -----------------------------
class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        email = request.data.get("email")

        # validation (basic but required)
        if not username or not password or not email:
            return Response(
                {"error": "All fields are required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        # check if user already exists
        if User.objects.filter(username=username).exists():
            return Response(
                {"error": "User already exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        # create user
        user = User.objects.create_user(
            username=username,
            password=password,
            email=email
        )

        # CELERY TASK (correct place)
        send_welcome_email.delay(user.email)

        return Response(
            {
                "message": "User registered successfully",
                "username": user.username,
                "email": user.email
            },
            status=status.HTTP_201_CREATED
        )