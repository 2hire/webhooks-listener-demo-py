import os
import logging
import config

import traceback

from flask import Flask, Blueprint, url_for, jsonify, g, session
from flask_restful import Api, Resource, abort
from flask_cors import CORS
from flask_opentracing import FlaskTracing
from wld.lib.exceptions import APIException

logging.basicConfig(level=int(os.environ.get("LOG_LEVEL", logging.INFO)),
                   format='[%(asctime)s]: {} %(levelname)s %(message)s'.format(os.getpid()),
                   datefmt='%Y-%m-%d %H:%M:%S',
                   handlers=[logging.StreamHandler()])

logger = logging.getLogger('waitress')

def create_app():

    logger.debug("Starting app")

    # create main blueprint
    api_bp = Blueprint("api", __name__)

    # create the api - flask_restful
    api = Api(api_bp)

    # Let's define a custom error handler of the API
    def custom_handle_error(self, e):
        abort(e.code, description=str(e))
    api.handle_error = custom_handle_error

    # create and configure the app
    app = Flask(__name__)
    app.config.from_object(config)
    CORS(app)

    # a simple page that says hello
    class Hello(Resource):
        def get(self):
            return {'Hello': 'World'}
    
    api.add_resource(Hello, '/hello')
    
    @app.errorhandler(Exception)
    def _handle_api_error(ex):

        if isinstance(ex, APIException):
            return jsonify(ex.to_dict()), ex.status_code
        else:
            logger.exception(ex)

            return jsonify({
                'title': "INTERNAL SERVER ERROR",
                'description': "Something went wrong handling the request: {}".format(type(ex)),
                'code': 201
            }), 500

    # Still outside the context.
    # Let's attach it to app
    with app.app_context():

        app.register_blueprint(api_bp, url_prefix=app.config['API_PREFIX'])

        from wld.blueprints import webhook_bp
        from wld.blueprints.routes import initialize_routes
        initialize_routes(api)

        app.register_blueprint(webhook_bp, url_prefix=app.config['API_PREFIX'])

    return app
