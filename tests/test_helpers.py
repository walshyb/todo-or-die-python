import pytest
from todo_or_die.helpers.generate_message import generate_message

def test_generates_message_without_date():
  result = generate_message("Message without date")

  assert result == "TODO, 'Message without date', was not completed. Get on this!"

def test_generates_message_with_date():
  result = generate_message("Message without date", "2021-09-08")

  assert result == "TODO, 'Message without date', was not completed by 2021-09-08. Get on this!"

