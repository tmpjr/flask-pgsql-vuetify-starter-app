# settings.py
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

# OR, the same with increased verbosity:
#load_dotenv(dotenv_path, verbose=True)

DEBUG=True
SECRET_KEY = os.environ.get('SECRET_KEY')
STATIC_FOLDER = os.environ.get('STATIC_FOLDER')
DB_NAME = os.environ.get('DB_NAME')
DB_USERNAME = os.environ.get('DB_USERNAME')
DB_PASSWORD = os.environ.get('DB_PASSWORD')
