from libs.utils.enums import ExtendedEnum


class Constants:

    class ElevatorStatus(ExtendedEnum):
        BUSY = "Busy"
        IDLE = "Idle"

    class ElevatorDoorStatus(ExtendedEnum):
        OPEN = 'Open'
        CLOSE = 'Close'



