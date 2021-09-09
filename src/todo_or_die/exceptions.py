from .helpers.generate_message import generate_message
from warnings import warn


class OverdueError(Exception):
    def __init__(self, message: str, date: str = ""):
        super().__init__(generate_message(message, date))

class OverdueWarning(Warning):
    def __init__(self, message, date):
        self.output = generate_message(message, date)
    
    def __str__(self):
        return repr(self.output)