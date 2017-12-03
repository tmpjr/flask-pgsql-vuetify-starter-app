#!/apps/env27/virtualenv/trabajando/bin/python
import sys
import logging
import os
import monitor
from dotenv import load_dotenv

APP_ROOT = os.path.join(os.path.dirname(__file__), '..')
dotenv_path = os.path.join('APP_ROOT', '.env')
load_dotenv(dotenv_path)

###
monitor.start(interval=1.0)
monitor.track(os.path.join(os.path.dirname(__file__), 'site.cf'))
###

logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/apps/env27/project/trabajando")
sys.path.insert(1,"/apps/env27/virtualenv/trabajando")

from app import app as application
application.secret_key = os.getenv('SECRET_KEY') 

