


from celery import shared_task


from django.core.mail import send_mail
from django.conf import settings

@shared_task
def send_registration_email(subject, message, recipient_list):
    send_mail(subject, message, settings.EMAIL_HOST_USER, recipient_list, fail_silently=False)
    return f"Email sent to {recipient_list}"