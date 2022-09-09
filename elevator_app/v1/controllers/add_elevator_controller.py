from elevator_app.db_managers.elevator import ElevatorDB


class AddElevatorController:

    def __init__(self, **payload):
        self.payload = payload

    def add_elevator(self):
        ElevatorDB().create_object(**self.payload)