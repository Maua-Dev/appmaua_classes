from src.helpers.errors.base_error import BaseError


class MissingParameters(BaseError):
    def __init__(self, message: str):
        super().__init__(f'Field {message} is missing.')

class WrongParameterType(BaseError):
    def __init__(self, parameter: str, wrongType: type, correctType: type):
        super().__init__(f'Field {parameter} has the wrong type ({wrongType.__name__}). Correct type: {correctType.__name__}.')