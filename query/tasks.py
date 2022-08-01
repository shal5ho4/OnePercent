from django.core.mail import send_mail
from kaikun.settings import EMAIL_HOST_USER
from .models import Query
from celery import task
import requests

@task
def query_received(query_id):
  sender = EMAIL_HOST_USER
  query = Query.objects.get(id=query_id)
  subject = f'お問い合わせNo.{query.id}'
  message = f'{query.name} 様 \n\n' \
            f'この度はお問い合わせいただき、ありがとうございます。\n' \
            f'担当者が内容を確認後、こちらからご連絡させていただきます。\n' \
            f'今しばらくお待ちくださいませ。\n\n' \
            f'株式会社 xxx'
  mail_sent = send_mail(
    subject, message, sender, [query.email]
  )
  return mail_sent


@task
def line_notify(query_id):
  query = Query.objects.get(id=query_id)
  line_notify_token = 'yKqKLHQzOCEjedKz6BQZJDxtZ6PFB8g63GoQjpjq9Vj'
  line_notify_api = 'https://notify-api.line.me/api/notify'

  message = f'問い合わせを受信しました。\n' \
            f'問い合わせNo.{query.id} \n' \
            f'送信者: {query.name} \n' \
            f'Email: {query.email} \n' \
            f'Tel: {query.phone} \n' \
            f'本文: {query.text}'
  payload = {'message': message}
  headers = {'Authorization': 'Bearer ' + line_notify_token}
  requests.post(line_notify_api, data=payload, headers=headers)