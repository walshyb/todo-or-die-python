import pytest
import warnings
from datetime import datetime as dt
from todo_or_die import todo_or_die
from todo_or_die.exceptions import OverdueError, OverdueWarning


DATE_FORMAT = "%Y-%m-%d"

def test_dies_with_overdue_string_date():
    with pytest.raises(OverdueError):
        todo_or_die("Message", "2020-09-08")

def test_dies_with_overdue_object_date():
    date = dt.strptime("2020-09-08", DATE_FORMAT)
    with pytest.raises(OverdueError):
        todo_or_die("Message", date)

def test_dies_with_missing_date():
  with pytest.raises(OverdueError):
        todo_or_die("Message")

def test_does_not_die_on_later_string_date():
    assert todo_or_die("Message", "2050-09-08") is None

def test_does_not_die_on_later_object_date():
    date = dt.strptime("2050-09-08", DATE_FORMAT)
    assert todo_or_die("Message", date) is None

def test_throws_warning_on_production(monkeypatch):
    monkeypatch.setenv('PRODUCTION', 'true')
    with pytest.warns(OverdueWarning):
        todo_or_die("Message", "2020-09-08")
    monkeypatch.delenv('PRODUCTION')