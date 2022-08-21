from django.db import models

from app.models._base import BaseModel


class Response(BaseModel):

    identifier = models.TextField()
    values = models.TextField()
    discord_guild = models.TextField()
    discord_author = models.TextField()
    discord_channel = models.TextField()
