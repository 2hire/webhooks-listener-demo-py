from marshmallow import ValidationError

from flask import make_response, request, g, current_app
from flask_restful import Resource

from wld.lib.exceptions import InvalidUsageException, TechnicalException

from wld.schema.requests.webhook_schema import WebhookSchema, GetWebhookSchema

from wld import logger
import hashlib
import hmac

class WebhookResource(Resource):

    def get(self):

        # request query parameters validation and getting challenge string
        challenge = GetWebhookSchema().load(request.args.to_dict())
        # logging challenge string on terminal
        logger.info
        logger.info("CHALLENGE: {}".format(challenge))

        return (challenge, 200)
    
    def post(self):

        # request body validation and parameters saved in bom
        try:
            bom = WebhookSchema().load(request.get_json())

        except ValidationError as err:
            raise InvalidUsageException(str(err.messages))

        logger.info("SIGNATURE:     {}".format(self._signature()))
        
        bom.print_info()
    
        return make_response({})

    def _signature(self):

        # TO BE TESTED AND COMPARED WITH HEADER X-HUB-SIGNATURE
        body = request.stream.read()
        secret = current_app.config["SECRET"].encode('utf-8')
        h = hmac.new(secret, body, hashlib.sha256)
        logger.info("SIGNATURE: {}".format(h.hexdigest()))
        # converti in binario x-hub-signature e compare without need of hexdigest()
        if not hmac.compare_digest(h.hexdigest(), request.headers['X-Hub-Signature']):
            logger.error("Not a valid signature")
            raise InvalidUsageException("Not a valid signature")

        return h.hexdigest()