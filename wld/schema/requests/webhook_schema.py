from marshmallow import fields, post_load, validates_schema, ValidationError, validate

from wld.schema.base_schema import BaseSchema
from wld.schema.requests.payload_schema import PayloadSchema

from wld.bom.webhook_bom import WebhookBom

from flask import current_app

TOPIC = ["online", "position", "distance_covered", "autonomy_percentage", "autonomy_meters"]
TYPE = ["generic", "specific"]

def validates_topic(data):
        topic = data.split(":")
        if len(topic)!=4:
            return False
        if topic[0]!="vehicle":
            return False
        if topic[2] not in TYPE:
            return False
        if topic[3] not in TOPIC:
            return False

class WebhookSchema(BaseSchema):

    _model = WebhookBom
    
    topic = fields.Str(required=True, validate=validates_topic)
    payload = fields.Nested(PayloadSchema, required=True)

    @post_load
    def make_webhook_bom(self, data, **kwargs):
        return self._model(**data)

class GetWebhookSchema(BaseSchema):

    mode = fields.Str(required=True, data_key="hub.mode", validate=lambda check: check=="subscribe")
    topic = fields.Str(required=True, data_key="hub.topic", validate=validate.OneOf(TOPIC))
    challenge = fields.Str(required=True, data_key="hub.challenge", validate=lambda check: check==current_app.config["SECRET"])

    @post_load
    def get_challenge(self, data, **kwargs):
        return data.get("challenge")
