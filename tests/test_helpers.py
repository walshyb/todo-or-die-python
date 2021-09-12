import pytest
from todo_or_die.helpers.generate_message import generate_message
from todo_or_die.helpers.is_production import is_production


def test_generates_message_without_date():
  result = generate_message("Message without date")

  assert result == "TODO, 'Message without date', was not completed. Get on this!"

def test_generates_message_with_date():
  result = generate_message("Message without date", "2021-09-08")

  assert result == "TODO, 'Message without date', was not completed by 2021-09-08. Get on this!"

def test_not_production_env():
  assert is_production() == False

def test_production_env(monkeypatch):
    monkeypatch.setenv('PRODUCTION', 'true')
    assert is_production() is True
    monkeypatch.delenv('PRODUCTION')

def test_django_env(monkeypatch):
    monkeypatch.setenv('DJANGO_ENVIRONMENT', 'production')
    assert is_production() is True
    monkeypatch.delenv('DJANGO_ENVIRONMENT')

def test_environment_env(monkeypatch):
    monkeypatch.setenv('ENVIRONMENT', 'production')
    assert is_production() is True
    monkeypatch.delenv('ENVIRONMENT')

def test_flask_env(monkeypatch):
    monkeypatch.setenv('FLASK_ENV', 'production')
    assert is_production() is True
    monkeypatch.delenv('FLASK_ENV')