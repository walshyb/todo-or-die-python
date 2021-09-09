import os

def is_production() -> bool:
  return os.getenv('PRODUCTION') == True \
          or os.getenv('DJANGO_ENVIRONMENT') == 'production' \
          or os.getenv('ENVIRONMENT') == 'production' \
          or os.getenv('FLASK_ENV') == 'production'
          