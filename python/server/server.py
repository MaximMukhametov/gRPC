import logging
from concurrent import futures

import grpc
from google.protobuf import any_pb2
from google.rpc import code_pb2, status_pb2, error_details_pb2

from python.proto import (GreeterServicer, HelloReply,
                          add_GreeterServicer_to_server)
from python.server.algorithm import product_of_tree_numbers


def create_greet_limit_exceed_error_status(name):
    detail = any_pb2.Any()
    detail.Pack(
        error_details_pb2.BadRequest(
            field_violations=[
                error_details_pb2.BadRequest.FieldViolation(
                    field='name',
                    description='This field can contain only array of integers,'
                                'like "1 6 3 4 5"')]))
    return status_pb2.Status(
        code=code_pb2.RESOURCE_EXHAUSTED,
        message='Request limit exceeded.',
        details=[detail],
    )


class Greeter(GreeterServicer):

    def SayHello(self, request, context):
        # rich_status = create_greet_limit_exceed_error_status(
        # request.name)
        # context.abort_with_status(rpc_status.to_status(rich_status))
        result = product_of_tree_numbers([1,3])
        return HelloReply(message='Hello sooqa, %s!' % result)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
