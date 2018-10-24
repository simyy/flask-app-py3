#!/usr/bin/env python
# encoding: utf-8

import os
import logging
import werkzeug
import werkzeug.debug
import werkzeug.serving
import demo

from flask_script  import Manager
from flask_script  import Shell
from flask_migrate import Migrate
from flask_migrate import MigrateCommand
from gevent.pywsgi import WSGIServer
from core.app import create_app
from core import exception
from core.app import db

app_name = os.getenv('FLASK_APP', 'flask_app')
app = create_app(os.getenv('FLASK_APP', 'flask_app'), os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
migrate = Migrate(app, db)


#LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
#DATE_FORMAT = "%m/%d/%Y %H:%M:%S %p"
#logging.basicConfig(level=logging.ERROR, format=LOG_FORMAT, datefmt=DATE_FORMAT)


def make_shell_context():
    return dict(app=app, db=db, demo=demo, exception=exception)

manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command("db", MigrateCommand)


@manager.command
def runserver(host="127.0.0.1", port=5000, env='product'):
    """
    run a gevent-based WSGI server
    """
    port = int(port)

    wrapped_app = app 
    if app.config.get("DEBUG", False):
        wrapped_app = werkzeug.debug.DebuggedApplication(app)

    server = WSGIServer(listener=(host, port), application=wrapped_app)


    def serve():
        app.logger.info(" * Running on http://%s:%d" % (host, port))
        server.serve_forever()

    if env == 'debug':
        from gevent import monkey
        monkey.patch_all()
        werkzeug.serving.run_with_reloader(serve, reloader_type="auto") 

    else:
        serve()


if __name__ == '__main__':
    manager.run()
