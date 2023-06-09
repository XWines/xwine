from app.common.constants import (
    DATA_KEY, ERROR_KEY, MESSAGE_KEY, STATUS_KEY,
    ERROR, SUCCESS, SOMETHING_WENT_WRONG
)


class BaseResponse:

    def __init__(self):
        self.response = {}

    def set_error_response(self, error_body: dict, message: str = SOMETHING_WENT_WRONG):
        self.response[STATUS_KEY] = ERROR
        self.response[MESSAGE_KEY] = message
        self.response[ERROR_KEY] = error_body
        self.response.pop(DATA_KEY, None)
        return self.response

    def set_success_response(self, data_body: dict, message: str = SUCCESS):
        self.response[STATUS_KEY] = SUCCESS
        self.response[MESSAGE_KEY] = message
        self.response[DATA_KEY] = data_body
        self.response.pop(ERROR_KEY, None)
        return self.response
