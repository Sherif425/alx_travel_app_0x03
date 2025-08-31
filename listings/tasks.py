from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings

@shared_task
def send_booking_confirmation_email(email, booking_reference):
    subject = "Booking Confirmation"
    message = f"Dear Customer,\n\nYour booking ({booking_reference}) has been confirmed.\n\nThank you for using ALX Travel!"
    from_email = settings.DEFAULT_FROM_EMAIL
    send_mail(subject, message, from_email, [email], fail_silently=False)
    return f"Booking confirmation email sent to {email}"
