from wld.bom.payload_bom import PayloadBom
from wld import logger

class WebhookBom:

    def __init__(self, mode=None, challenge=None, topic=None, payload=None, uuid=None, type=None, name=None):

        self._mode = mode
        self._challenge = challenge
        self._topic = topic
        self._payload = payload
        self._uuid = uuid
        self._type = type
        self._name = name
    
    def print_info(self):

        logger.info("VEHICLE:       {}".format(self._uuid))
        logger.info("SIGNAL_TYPE:   {}".format(self._type))
        logger.info("SIGNAL NAME:   {}".format(self._name))

        if self._name == "position":
            logger.info("VALUE: ")
            logger.info("   Latitude:   {}°".format(self._payload.data.latitude))
            logger.info("   Longitude:  {}°".format(self._payload.data.longitude))
        elif self._name == "autonomy_percentage":
            logger.info("VALUE:         {} %".format(self._payload.data.percentage))
        elif self._name == "autonomy_meters":
            logger.info("VALUE:         {} meters".format(self._payload.data.meters))
        elif self._name == "distance_covered":
            logger.info("VALUE:         {} meters".format(self._payload.data.meters))
        elif self._name == "online":
            logger.info("VALUE:         {}".format(self._payload.data.online))
        logger.info(" ")    

    @property
    def mode(self) -> str:
        return self._mode

    @mode.setter
    def mode(self, mode: str):
        self._mode = mode

    @property
    def challenge(self) -> str: 
        return self._challenge

    @challenge.setter
    def challenge(self, challenge: str):
        self._challenge = challenge

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
        
    @property
    def uuid(self) -> str:
        return self._uuid

    @uuid.setter
    def uuid(self, uuid: str):
        self._uuid = uuid

    @property
    def type(self) -> str:
        return self._type

    @type.setter
    def type(self, type: str):
        self._type = type

    @property
    def name(self) -> float: 
        return self._name

    @name.setter
    def name(self, name: float):
        self._name = name
