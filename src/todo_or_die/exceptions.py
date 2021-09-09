from .helpers.generate_message import generate_message


class OverdueError(Exception):
    def __init__(self, message: str, date: str = ""):
        super().__init__(generate_message(message, date))

class OverdueWarning(Warning):
    pass