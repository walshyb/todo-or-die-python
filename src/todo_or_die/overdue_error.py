class OverdueError(Exception):
    def __init__(self, date, message=""):
        message = f", {message}," if message else ""
        super().__init__(f"Todo{message} was not completed by {date}. Get on this!")
