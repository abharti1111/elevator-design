from elevator_app.models import Elevator
from libs.utils.base_db_manager import BaseDBManager


class ElevatorDB(BaseDBManager):
    model = Elevator
    has_active_filter = True
