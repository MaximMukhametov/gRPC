import logging
from concurrent import futures

import grpc
from grpc_status import rpc_status

from python.proto import (CalculateMultiplicationServicer,
                          add_CalculateMultiplicationServicer_to_server,
                          Response)
from python.server.algorithm import maximum_product_of_tree_numbers
from python.server.errors import create_error_array_field_status


class CalculateMultiplication(CalculateMultiplicationServicer):

    def Calculate(self, request, context):
        try:
            # trying to convert a string of numbers to array of numbers
            array_of_int = [float(item) for item in request.array.split()]
        except ValueError:
            error_status = create_error_array_field_status(request.array)
            context.abort_with_status(rpc_status.to_status(error_status))
        result = maximum_product_of_tree_numbers(array_of_int)
        return Response(result=result)


def serve(port):
    server = grpc.server(futures.ThreadPoolExecutor())
    add_CalculateMultiplicationServicer_to_server(CalculateMultiplication(),
                                                  server)
    server.add_insecure_port(f'[::]:{port}')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    server_port = 50051
    logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                        level=logging.INFO)
    logging.info(f"The server started listening "
                 f"for rpc-requests on the port:{server_port} ")
    serve(server_port)
