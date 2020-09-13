from google.protobuf import any_pb2
from google.rpc import code_pb2, status_pb2, error_details_pb2


def create_error_array_field_status(value):
    """
    Creating a response rpc-status for an incorrect field.
    """
    detail = any_pb2.Any()
    detail.Pack(
        error_details_pb2.BadRequest(
            field_violations=[
                error_details_pb2.BadRequest.FieldViolation(
                    field='array',
                    description="This field can contain only array "
                                "containing at least 3 elements(int or float) "
                                "separated by spaces, like `1 0 3.4 -4 5`")]))
    return status_pb2.Status(
        code=code_pb2.INVALID_ARGUMENT,
        message=f"Unable to calculate the result from: {value}",
        details=[detail],
    )
