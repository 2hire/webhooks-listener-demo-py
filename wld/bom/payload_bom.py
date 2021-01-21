from wld.bom.data_bom import DataBom


class PayloadBom:

    def __init__(self, data=None, timestamp = None, delivery_timestamp=None):

        self._data = data
        self._timestamp = timestamp
        self._delivery_timestamp = delivery_timestamp

    @property
    def data(self) -> DataBom:
        return self._data

    @data.setter
    def data(self, data: DataBom):
        self._data = data

    @property
    def timestamp(self) -> int:
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp: int):
        self._timestamp = timestamp

    @property
    def delivery_timestamp(self) -> int:
        return self._delivery_timestamp

    @delivery_timestamp.setter
    def delivery_timestamp(self, delivery_timestamp: int):
        self._delivery_timestamp = delivery_timestamp

