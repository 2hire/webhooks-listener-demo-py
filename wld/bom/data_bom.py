class DataBom:

    def __init__(self, online=None, latitude=None, longitude=None, meters=None, percentage=None):

        self._online = online
        self._latitude = latitude
        self._longitude = longitude
        self._meters = meters
        self._percentage = percentage
        
    @property
    def online(self) -> bool:
        return self._online

    @online.setter
    def online(self, online: bool):
        self._online = online

    @property
    def latitude(self) -> float:
        return self._latitude

    @latitude.setter
    def latitude(self, latitude: float):
        self._latitude = latitude

    @property
    def longitude(self) -> float: 
        return self._longitude

    @longitude.setter
    def longitude(self, longitude: float):
        self._longitude = longitude

    @property
    def meters(self) -> int:
        return self._meters

    @meters.setter
    def meters(self, meters: int):
        self._meters = meters

    @property
    def percentage(self) -> int: 
        return self._percentage

    @percentage.setter
    def percentage(self, percentage: int):
        self._percentage = percentage
