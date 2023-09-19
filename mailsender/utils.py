from django.conf import settings
from django.core.mail import send_mail
from django.utils import timezone

from mailsender.models import Mailing, MailingLogs


def send_mailing():
    now = timezone.now()

    clients = Mailing.client
    mailing_to_send = Mailing.objects.exclude(status='completed')
    for mailing in mailing_to_send:
        if mailing.get_status() == 'running':
            try:
                result = send_mail(
                    subject=mailing.title,
                    message=mailing.body,
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[clients]
                )
                status = 'ok'
            except:
                result = False
                status = 'failed'
            mailing_log = MailingLogs.objects.create(mailing=mailing, last_try=now, status=status)
            mailing_log.save()


