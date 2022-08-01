from django.db import models

class Query(models.Model):
  name = models.CharField(max_length=30)
  email = models.EmailField()
  phone = models.CharField(max_length=15, blank=True)
  text = models.TextField()
  created = models.DateTimeField(auto_now_add=True)

  class Meta:
    ordering = ('-created',)
    verbose_name_plural = 'queries'

  def __str__(self):
    return f'問い合わせ#{self.id}'

