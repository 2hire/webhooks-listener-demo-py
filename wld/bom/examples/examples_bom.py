class ExamplesBom:

    def __init__(self, params=None):

        self._params = params
        

    @property
    def params(self) -> str:
        return self._params

    @params.setter
    def params(self, params: str):
        self._params = params
