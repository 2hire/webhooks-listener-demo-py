from marshmallow import ValidationError

from flask import make_response, request
from flask_restful import Resource

from flask_be_template.lib.exceptions import InvalidUsageException, TechnicalException

from flask_be_template.schema.requests.examples.examples_request_schema import ExamplesRequestSchema


class ExamplesResource(Resource):

    def get(self):

        response = {'GET': 'examples'}

        return make_response(response)
    
    def post(self):
        
        try:
            bom = ExamplesRequestSchema().load(request.get_json())

        except ValidationError as err:
            raise InvalidUsageException(str(err.messages))

        response = bom

        return make_response(response)
