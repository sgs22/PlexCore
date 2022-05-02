from django.db import models
from django.contrib.auth.models import User


class MediaRequest(models.Model):
    request_title = models.CharField(max_length=255)
    request_description = models.TextField(max_length=2048)
    request_link_media = models.URLField()
    request_user = models.ForeignKey(to=User, on_delete=models.CASCADE)
