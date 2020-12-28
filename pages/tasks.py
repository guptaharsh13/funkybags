from celery import shared_task

from django.core.mail import EmailMessage
from django.conf import settings

@shared_task
def sendEmail(subject, body, recipient):
    email = EmailMessage(
        subject,
        body,
        settings.EMAIL_HOST_USER,
        [recipient]
    )
    email.send()
    return None