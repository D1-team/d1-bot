from django.db import models

from app.models._base import BaseModel


class Response(BaseModel):

    identifier = models.TextField()
    values = models.TextField()
    discord_server = models.TextField()
    discord_user = models.TextField()
    discord_channel = models.TextField()
