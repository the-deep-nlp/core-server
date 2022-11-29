from rest_framework.views import exception_handler
from rest_framework.exceptions import ValidationError


def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)

    if isinstance(exc, ValidationError):
        field_errors = response.data
        response.data = {
            "status": "fail",
            "field_errors": field_errors,
            "message": "Invalid parameters",
        }
    else:
        response.data["status"] = "fail"
        response.data["message"] = "Client error"  # TODO: fix this
    if response is not None:
        response.data["status_code"] = response.status_code

    return response
