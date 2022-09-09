from django.db import models

from elevator_app.models import Elevator
from libs.abstract_base_model import BaseModel


class Requests(BaseModel):
    elevator = models.ForeignKey(Elevator, on_delete=models.DO_NOTHING)
    source_floor = models.IntegerField()
    destination_floor = models.IntegerField()

