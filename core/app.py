#!/usr/bin/env python
# encoding: utf-8

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import configs


db = SQLAlchemy()


def create_app(app_name, config_name):
    #app = Flask(app_name, template_folder="app/templates")
    app = Flask(app_name)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    if config_name == 'production':
        app.config['DEBUG'] = False

    # @app.route('/static/<path:path>')
    # def static_files():
    #     return app.send_static_file(path)

    # init environment
    app.config.from_object(configs[config_name])
    db.init_app(app)
   
    # attack routes and cunstom err pages here
    from demo import demo as demo_blueprint
    app.register_blueprint(demo_blueprint, url_prefix='/')


    return app
