import logging

from django.db import models

logger = logging.getLogger(__name__)


class BaseModel(models.Model):
    """Base model to define the common columns and managers."""

    id = models.BigAutoField(primary_key=True)
    deleted = models.BooleanField(default=False, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        """BaseModel Meta class."""

        abstract = True
