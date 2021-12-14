# Copyright Contributors to the Amundsen project.
# SPDX-License-Identifier: Apache-2.0

import ast
import logging
import logging.config
import os

from flask import Flask, Blueprint

from werkzeug.middleware.proxy_fix import ProxyFix

from app.api import init_routes
from app.api.v0 import blueprint

PROJECT_ROOT = os.getenv('PROJECT_ROOT', os.path.dirname(os.path.abspath(__file__)))
static_dir = os.path.join(PROJECT_ROOT, 'static')


def create_app(config_module_class: str, template_folder: str = None) -> Flask:
    """ Support for importing arguments for a subclass of flask.Flask """
    args = ast.literal_eval(os.getenv('APP_WRAPPER_ARGS', '')) if os.getenv('APP_WRAPPER_ARGS') else {}

    tmpl_dir = template_folder if template_folder else os.path.join(PROJECT_ROOT, static_dir, 'dist/templates')
    app = Flask(__name__, static_folder=static_dir, template_folder=tmpl_dir, **args)

    """ Support for importing a custom config class """
    config_module_class = \
        os.getenv('FRONTEND_SVC_CONFIG_MODULE_CLASS') or config_module_class

    app.config.from_object(config_module_class)
    app.wsgi_app = ProxyFix(app.wsgi_app)

    if app.config.get('LOG_CONFIG_FILE'):
        logging.config.fileConfig(app.config.get('LOG_CONFIG_FILE'), disable_existing_loggers=False)
    else:
        logging.basicConfig(format=app.config.get('LOG_FORMAT'), datefmt=app.config.get('LOG_DATE_FORMAT'))
        logging.getLogger().setLevel(app.config.get('LOG_LEVEL'))

    logging.info('Created app with config name {}'.format(config_module_class))
    logging.info('Using search service at {}'.format(app.config.get('SEARCHSERVICE_BASE')))

    api_bp = Blueprint('api', __name__)

    app.register_blueprint(blueprint)
    app.register_blueprint(api_bp)
    init_routes(app)

    init_custom_routes = app.config.get('INIT_CUSTOM_ROUTES')
    if init_custom_routes:
        init_custom_routes(app)

    return app
