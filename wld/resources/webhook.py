from marshmallow import ValidationError

from flask import make_response, request, g
from flask_restful import Resource

from wld.lib.exceptions import InvalidUsageException, TechnicalException

from wld.schema.requests.webhook_schema import WebhookSchema, GetWebhookSchema

from wld import logger


class WebhookResource(Resource):

    def get(self):

        challenge = GetWebhookSchema().load(request.args.to_dict())

        logger.info(challenge)

        return make_response({})
    
    def post(self):

        try:
            bom = WebhookSchema().load(request.get_json())

        except ValidationError as err:
            raise InvalidUsageException(str(err.messages))
        
        bom.print_info()

        return make_response({})
