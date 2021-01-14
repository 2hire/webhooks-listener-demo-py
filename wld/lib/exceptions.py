class APIException(Exception):
    
    def __init__(self, description, error, status_code):
        Exception.__init__(self)

        self._description = description
        self._error = error
        self._status_code = status_code
        self._title = "UNKNOWN ERROR"

    def to_dict(self):

        d = {}

        d['title'] = self.title
        d['description'] = self.description
        d['error'] = self.error

        return d
    
    @property
    def description(self) -> str:
        return self._description
    
    @description.setter
    def description(self, description: str):
        self._description = description
    
    @property
    def error(self) -> int:
        return self._error
    
    @error.setter
    def error(self, error: int):
        self._error = error
    
    @property
    def status_code(self) -> int:
        return self._status_code
    
    @status_code.setter
    def status_code(self, status_code: int):
        self._status_code = status_code
    
    @property
    def title(self) -> str:
        return self._title
    
    @title.setter
    def title(self, title: str):
        self._title = title

class InvalidUsageException(APIException):

    def __init__(self, description):
        APIException.__init__(self, description, 100, 400)
        self._title = 'INVALID API USAGE ERROR'

class TechnicalException(APIException):

    def __init__(self, description):
        APIException.__init__(self, description, 200, 500)
        self._title = 'TECHNICAL ERROR'

