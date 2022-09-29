from datetime import datetime
from xmlrpc.client import DateTime
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

class Task(models.Model):
    user = models.ForeignKey(User, models.SET_NULL, blank=True, null=True)
    date = models.DateTimeField(default=datetime.now())
    title = models.TextField()
    description = models.TextField()
    is_finished = models.BooleanField(default=False)

