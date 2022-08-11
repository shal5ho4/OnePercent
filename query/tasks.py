from django.core.mail import send_mail
from .models import Query
from celery import task
from kaikun.settings import EMAIL_HOST_USER, LINE_NOTIFY_TOKEN_2
# from email.mime.text import MIMEText
# from email.utils import formatdate
import requests
# import smtplib


@task
def query_received(query_id):
  query = Query.objects.get(id=query_id)

  sender = EMAIL_HOST_USER
  subject = f'株式会社OnePercent 受付No.{query.id}'
  body = f'\n{query.name} 様 \n\n' \
         f'この度はお問い合わせいただき、ありがとうございます。\n' \
         f'お客様のお問い合わせの受付が完了しました。\n' \
         f'担当者が内容を確認後、こちらからご連絡させていただきます。\n\n' \
         f'少人数で営業している都合上、返答にお時間頂く場合がございます。\n' \
         f'恐れ入りますが、お急ぎの場合は一度お電話くださいませ。\n' \
         f'よろしくお願い申し上げます。\n\n' \
         f'株式会社 OnePercent'

  mail_sent = send_mail(
    subject, body, sender, [query.email]
  )
  return mail_sent


@task
def line_notify(query_id):
  query = Query.objects.get(id=query_id)
  line_notify_api = 'https://notify-api.line.me/api/notify'

  message = f'問い合わせを受信しました。\n' \
            f'問い合わせNo.{query.id} \n' \
            f'送信者: {query.name} \n' \
            f'Email: {query.email} \n' \
            f'Tel: {query.phone} \n' \
            f'本文: {query.text}'
  payload = {'message': message}
  headers = {'Authorization': 'Bearer ' + LINE_NOTIFY_TOKEN_2}
  requests.post(line_notify_api, data=payload, headers=headers)
  