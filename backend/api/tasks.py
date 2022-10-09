from django.core.mail import send_mail
from backend.settings import EMAIL_HOST_USER
from celery import shared_task

# def sendMail(subject, message, receivers):
#     send_mail(subject,message,EMAIL_HOST_USER,[receivers],
#     fail_silently= True)


@shared_task(bind=True)
# def sendMail(self):
def sendMail(self, subject, message, receivers):
    try:
        send_mail(subject, message, EMAIL_HOST_USER, [receivers], fail_silently= False)

    except Exception as e:
        return f"⭐ '{e}'"
    
    return "Done"