from django.db import models

from libs.abstract_base_model import BaseModel


class Elevator(BaseModel):
    is_operational = models.BooleanField(default=True)
    status = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
