from marshmallow import ValidationError

from flask import make_response, request, g, current_app
from flask_restful import Resource

from wld.lib.exceptions import InvalidUsageException, TechnicalException

from wld.schema.requests.listener_schema import PostListenerSchema, GetListenerSchema

from wld import logger
import hashlib
import hmac

class ListenerResource(Resource):

    def get(self):

        # request query parameters validation and getting challenge string
        try:
            bom = GetListenerSchema().load(request.args.to_dict())
        except ValidationError as err:
            logger.error("VALIDATION: {}".format(str(err.messages)))
            raise InvalidUsageException(str(err.messages))

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
            bom = PostListenerSchema().load(request.get_json())
        except ValidationError as err:
            logger.error("VALIDATION: {}".format(str(err.messages)))
            raise InvalidUsageException(str(err.messages))
        
        # log info on terminal
        self.print_info(bom)
    
        return make_response({})

    def print_info(self, bom):

        logger.info(" ")
        logger.info("SIGNATURE:     {}".format(self._signature()))
        logger.info("VEHICLE:       {}".format(bom.uuid))
        logger.info("SIGNAL TYPE:   {}".format(bom.type))
        logger.info("SIGNAL NAME:   {}".format(bom.name))

        if bom.name == "position":
            logger.info("VALUE: ")
            logger.info("   Latitude:   {}°".format(bom.payload.data.latitude))
            logger.info("   Longitude:  {}°".format(bom.payload.data.longitude))
        
        elif bom.name == "autonomy_percentage":
            logger.info("VALUE:         {}%".format(bom.payload.data.percentage))
        elif bom.name == "autonomy_meters":
            logger.info("VALUE:         {}m".format(bom.payload.data.meters))
        elif bom.name == "distance_covered":
            logger.info("VALUE:         {}m".format(bom.payload.data.meters))
        elif bom.name == "online":
            logger.info("VALUE:         {}".format(bom.payload.data.online))


    def _signature(self):

        body = request.data
        secret = current_app.config["SECRET"].encode('utf-8')
        h = hmac.new(secret, body, hashlib.sha256).hexdigest()

        signature = request.headers.get('X-Hub-Signature', '')

        if not hmac.compare_digest("sha256="+h, signature):
            logger.error("NOT A VALID SIGNATURE: {}".format(signature))
            raise InvalidUsageException("Not a valid signature")

        return h
    