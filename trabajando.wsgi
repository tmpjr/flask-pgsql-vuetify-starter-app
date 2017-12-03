#!/apps/env27/virtualenv/trabajando/bin/python
import sys
import logging

###
import os
import monitor
monitor.start(interval=1.0)
monitor.track(os.path.join(os.path.dirname(__file__), 'site.cf'))
###

logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/apps/env27/project/trabajando")
sys.path.insert(1,"/apps/env27/virtualenv/trabajando")

from app import app as application
application.secret_key = '\xce\xdc\xd4\xe4\x0f\xa7;e=\x8f\xbcT\x87e&\x89q\x93t\x16\xb5\x00\x85\x89'

