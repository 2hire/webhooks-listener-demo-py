from marshmallow import fields, post_load, validates_schema, ValidationError

from wld.schema.base_schema import BaseSchema

from wld.bom.data_bom import DataBom

class DataSchema(BaseSchema):

    _model = DataBom
    
    online = fields.Bool()
    latitude = fields.Float()
    longitude = fields.Float()
    meters = fields.Int()
    percentage = fields.Int()

    @post_load
    def make_data_bom(self, data, **kwargs):
        return self._model(**data)    
