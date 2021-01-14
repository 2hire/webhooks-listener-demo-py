from marshmallow import fields, post_load, validates_schema, ValidationError

from flask_be_template.schema.base_schema import BaseSchema

from flask_be_template.bom.examples.examples_bom import ExamplesBom

class ExamplesRequestSchema(BaseSchema):

    _model = ExamplesBom
    
    param = fields.Str(required=True)

    @post_load
    def make_examples_bom(self, data, **kwargs):
        return self._model(**data)