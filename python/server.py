from concurrent import futures

import grpc
from core import logging_of_called_rpc_functions
from core import (maximum_product_of_tree_numbers,
                  create_error_array_field_status)
from grpc_status import rpc_status

from proto import (CalculateProductOfTripletServicer, Response,
                   add_CalculateProductOfTripletServicer_to_server)


class CalculateProductOfTriplet(CalculateProductOfTripletServicer):

    @logging_of_called_rpc_functions
    def CalculateMaxTriplet(self, request, context):
        """
        Calculate maximum product of three numbers in an array.
        This function can be called by a grpc-client
        written in any programming language.
        """
        try:
            # Trying to convert a string of numbers to array
            # of numbers and calculate maximum product of triplet.
            array_of_int = [float(item) for item in request.array.split()]
            result = maximum_product_of_tree_numbers(array_of_int)
        except ValueError:
            error_status = create_error_array_field_status(request.array)
            context.abort_with_status(rpc_status.to_status(error_status))

        return Response(result=result)


def serve(port):
    """Creates a server with which RPCs can be serviced."""
    server = grpc.server(futures.ThreadPoolExecutor())
    add_CalculateProductOfTripletServicer_to_server(CalculateProductOfTriplet(),
                                                    server)
    server.add_insecure_port(f'[::]:{port}')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    server_port = 50051
    print(f"The server started listening for "
          f"rpc-requests on the port:{server_port} ")
    serve(server_port)
