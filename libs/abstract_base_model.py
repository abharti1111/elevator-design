import uuid

from django.db import models
from jsonfield import JSONField


class BaseModel(models.Model):
    id = models.UUIDField(default=uuid.uuid4(), primary_key=True, auto_created=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(null=True)
    meta_data = JSONField(null=True)

    class Meta:
        abstract = True
