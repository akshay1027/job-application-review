from django.core.mail import send_mail
from backend.settings import EMAIL_HOST_USER
from celery import shared_task

# def sendMail(subject, message, receivers):
#     send_mail(subject,message,EMAIL_HOST_USER,[receivers],
#     fail_silently= True)


@shared_task(bind=True)
def sendMail(self, subject, message, receivers):
    try:
        # send_mail(subject, message, 'akshayar1027@gmail.com', 'akshayar1027@gmail.com', fail_silently= False)
        send_mail(subject, message, 'akshayar1027@gmail.com', [receivers], fail_silently= False)
        # message = "If you are liking my content, please hit the like button and do subscribe to my channel"
        # to_email = user.email
        # send_mail(
        #     subject=mail_subject,
        #     message=message,
        #     from_email=settings.EMAIL_HOST_USER,
        #     recipient_list=[to_email],
        #     fail_silently=False,
        # )
        # for i in range(1000):
        #     print("Done sending mail")

    except Exception as e:
        return f"details: '{e}'"
    
    return "Done"