import datetime

from django.db import models
from django.utils import timezone


class Message(models.Model):
    message_name = models.CharField(max_length=200)
    message_contact = models.CharField(max_length=200)
    message_body = models.CharField(max_length=400)
    pub_date = models.DateTimeField('date submitted')

    def __str__(self):
	return self.message_name

    def was_published_recently(self):
	return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'
