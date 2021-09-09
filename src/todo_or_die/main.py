import os
from .exceptions import OverdueError
from .exceptions import OverdueWarning
from .helpers import is_production
from datetime import datetime as dt
from typing import Union
from warnings import warn

DATE_FORMAT = "%Y-%m-%d"


def todo_or_die(message: str, by: Union[str, dt] = None) -> None:
    if not by:
        __die(message)

    if isinstance(by, str):
        by = dt.strptime(by, DATE_FORMAT)

    if dt.now() > by:
        __die(message, by.strftime(DATE_FORMAT))


def __die(message: str, date: str = "") -> None:
    if is_production():
        warn('', OverdueWarning)
    else:
        raise OverdueError(message, date)
