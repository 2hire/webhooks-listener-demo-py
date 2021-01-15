from marshmallow import fields, post_load, validates_schema, ValidationError

from wld.schema.base_schema import BaseSchema
from wld.schema.requests.payload_schema import PayloadSchema

from wld.bom.webhook_bom import WebhookBom

class WebhookSchema(BaseSchema):

    _model = WebhookBom
    
    topic = fields.Str(required=True)
    payload = fields.Nested(PayloadSchema, required=True)

    @post_load
    def make_webhook_bom(self, data, **kwargs):
        return self._model(**data)