from datetime import datetime
from smtplib import SMTPException

from django.conf import settings
from django.core.mail import send_mail

from mailings.models import Mailing, Client, MailingLog


def check_mailings():
    mailings_list = Mailing.objects.filter(status='started').exclude(owner__status='blocked')

    print('now', datetime.utcnow().time())
    print('now', datetime.utcnow().date())
    for mailing in mailings_list:
        is_sending_time = mailing.sending_time_start <= datetime.now().time() <= mailing.sending_time_end

        if is_sending_time:
            send_mailing(mailing)
            if mailing.periodicity == 'once':
                check_to_done_once_mailing(mailing)


def send_mailing(mailing: Mailing):
    if mailing.periodicity == 'daily':
        min_delta_day = 1
    elif mailing.periodicity == 'weekly':
        min_delta_day = 7
    elif mailing.periodicity == 'monthly':
        min_delta_day = 30

    print(mailing)
    for client in mailing.client_set.all():
        print(client)
        last_letter_log = mailing.mailinglog_set.filter(client=client, status='success').order_by(
            '-mailing_date').first()
        is_need_letter = False
        if not last_letter_log:
            is_need_letter = True
        elif mailing.periodicity != 'once':
            delta = datetime.utcnow().date() - last_letter_log.mailing_date
            print(delta.days)
            if delta.days >= min_delta_day:
                is_need_letter = True

        print(is_need_letter)
        if is_need_letter:
            send_letter(mailing, client)


def send_letter(mailing: Mailing, client: Client):
    try:
        send_mail(
            subject=mailing.mail_title,
            message=mailing.mail_content,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[client.email],
        )
        MailingLog.objects.create(
            mailing_date=datetime.utcnow().date(),
            mailing_time=datetime.utcnow().time(),
            status='success',
            mailing=mailing,
            client=client,
        )
    except SMTPException as err:
        MailingLog.objects.create(
            mailing_date=datetime.utcnow().date(),
            mailing_time=datetime.utcnow().time(),
            status='fail',
            server_ans=err,
            mailing=mailing,
            client=client,
        )


def check_to_done_once_mailing(mailing: Mailing):
    is_done = True
    for client in mailing.client_set.all():
        log = mailing.mailinglog_set.filter(client=client, status='success')

        if not log:
            is_done = False

    if is_done:
        mailing.status = 'done'
        mailing.save()
    print(mailing, is_done)
