from marshmallow import ValidationError

from flask import make_response, request, g, current_app
from flask_restful import Resource

from wld.lib.exceptions import InvalidUsageException, TechnicalException

from wld.schema.requests.webhook_schema import PostWebhookSchema, GetWebhookSchema

from wld import logger
import hashlib
import hmac

class WebhookResource(Resource):

    def get(self):

        # request query parameters validation and getting challenge string
        bom = GetWebhookSchema().load(request.args.to_dict())

        # logging challenge string on terminal
        logger.info(" ")
        logger.info("Hello, you have subscribed to get information about the topic: {}".format(bom.name))
        logger.info("The challenge string is: {}".format(bom.challenge))
    
        # prepare response
        response = make_response(bom.challenge, 200)
        response.mimetype = "text/plain"
        
        return response
    
    def post(self):

        # request body validation and parameters saved in bom
        try:
            bom = PostWebhookSchema().load(request.get_json())

        except ValidationError as err:
            logger.info("ERROR VALIDATION: {}".format(str(err.messages)))
            raise InvalidUsageException(str(err.messages))
        
        logger.info(" ")
        logger.info("SIGNATURE:     {}".format(self._signature()))
        
        bom.print_info()
    
        return make_response({})

    def _signature(self):

        body = request.data
        secret = current_app.config["SECRET"].encode('utf-8')
        h = hmac.new(secret, body, hashlib.sha256).hexdigest()

        signature = request.headers.get('X-Hub-Signature', 'sha256==')[7:]

        # converti in binario x-hub-signature e compare without need of hexdigest()
        if not hmac.compare_digest(h, signature):
            logger.error("Not a valid signature: {}".format(signature))
            raise InvalidUsageException("Not a valid signature")

        return h