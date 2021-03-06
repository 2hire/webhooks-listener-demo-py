from marshmallow import fields, post_load, validates_schema, ValidationError, validate

from wld.schema.base_schema import BaseSchema
from wld.schema.requests.payload_schema import PayloadSchema

from wld.bom.listener_bom import ListenerBom

from flask import current_app

SIGNAL_TYPE = ["generic"]
SIGNAL_NAME = ["online", "position", "distance_covered", "autonomy_percentage", "autonomy_meters", "*"]

def validates_topic(_topic):
        topic = _topic.split(":")
        if len(topic)!=4:
            return False
        if topic[0]!="vehicle":
            return False
        if topic[2] not in SIGNAL_TYPE:
            return False
        if topic[3] not in SIGNAL_NAME:
            return False


class BaseListenerSchema(BaseSchema):

    _model = ListenerBom

    @post_load
    def make_listener_bom(self, data, **kwargs):
        topic = data.get("topic").split(":")
        data.update({
            "uuid": topic[1],
            "type": topic[2],
            "name": topic[3]
        })
        return self._model(**data)

class GetListenerSchema(BaseListenerSchema):

    mode = fields.Str(required=True, data_key="hub.mode", validate=lambda check: check=="subscribe")
    topic = fields.Str(required=True, data_key="hub.topic", validate=validates_topic)
    challenge = fields.Str(required=True, data_key="hub.challenge")


class PostListenerSchema(BaseListenerSchema):
    
    topic = fields.Str(required=True, validate=validates_topic)
    payload = fields.Nested(PayloadSchema, required=True)

