from flask_restful import abort

class HttpError:
    def __init__(self, status_code, message):
        self.status_code = status_code
        self.message = message

    def raise_error(self, error_type, identifier=None):
        error_message = ""
        if error_type == "not_found":
            error_message = f"{self.message} {identifier} not found"
        elif error_type == "already_exists":
            error_message = f"{self.message} {identifier} already exists"
        else:
            error_message = f"{self.message} An error occurred"

        abort(self.status_code, message=error_message)
