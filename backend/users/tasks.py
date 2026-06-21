from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_welcome_email(email):
    send_mail(
        "Welcome!",
        "Thanks for registering in Library System.",
        "marivar2018@gmail.com",
        [email],
        fail_silently=True,
    )