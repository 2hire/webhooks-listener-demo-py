from wld.bom.payload_bom import PayloadBom
from wld import logger

class WebhookBom:

    def __init__(self, topic=None, payload=None):

        self._topic = topic
        self._payload = payload

    def print_info(self):

        vehicle = self._topic.split(':')
        name = vehicle[3]

        logger.info("VEHICLE UUID:          {}".format(vehicle[1]))

        if name == "position":
            logger.info("POSITION: ")
            logger.info("   Latitude:           {}".format(self._payload.data.latitude))
            logger.info("   Longitude:          {}".format(self._payload.data.longitude))
        elif name == "autonomy_percentage":
            logger.info("AUTONOMY_PERCENTAGE:   {}".format(self._payload.data.percentage))
        elif name == "autonomy_meters":
            logger.info("AUTONOMY_METERS:       {}".format(self._payload.data.meters))
        elif name == "distance_covered":
            logger.info("DISTANCE_COVERED:      {}".format(self._payload.data.meters))
        elif name == "online":
            logger.info("ONLINE:                {}".format(self._payload.data.online))
        

    @property
    def topic(self) -> str: 
        return self._topic

    @topic.setter
    def topic(self, topic: str):
        self._topic = topic

    @property
    def payload(self) -> PayloadBom:
        return self._payload

    @payload.setter
    def payload(self, payload: PayloadBom):
        self._payload = payload

