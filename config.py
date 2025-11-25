# config.py
import os

API_KEY = os.getenv('API_KEY', 'default-api-key')
DEBUG_MODE = os.getenv('DEBUG_MODE', 'false').lower() == 'true'
DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///local.db')
