from marshmallow import fields, post_load, validates_schema, ValidationError

from wld.schema.base_schema import BaseSchema
from wld.schema.requests.data_schema import DataSchema

from wld.bom.payload_bom import PayloadBom

class PayloadSchema(BaseSchema):

    _model = PayloadBom
    
    data = fields.Nested(DataSchema, required=True)
    timestamp = fields.Int()

    @post_load
    def make_payload_bom(self, data, **kwargs):
        return self._model(**data)