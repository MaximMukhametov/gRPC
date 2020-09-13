import logging

import grpc
from google.rpc import error_details_pb2
from grpc_status import rpc_status

from proto import Request, CalculateProductOfTripletStub

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO)


def process(stub):
    """Call a specific function on the server"""
    try:
        response = stub.CalculateMaxTriplet(Request(array=input()))
        logging.info('Call success: %.2f', response.result)
    except grpc.RpcError as rpc_error:
        logging.error('Call failure:\n code: %s \n details: %s',
                      rpc_error.code(),
                      rpc_error.details())
        status = rpc_status.from_call(rpc_error)
        for detail in status.details:
            if detail.Is(error_details_pb2.BadRequest.DESCRIPTOR):
                info = error_details_pb2.BadRequest()
                detail.Unpack(info)
                logging.error('Bad request: %s', info)
            else:
                raise RuntimeError('Unexpected failure: %s' % detail)


def main():
    """
    Creates an insecure Channel to a server.
    The returned Channel is thread-safe.
    """
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = CalculateProductOfTripletStub(channel)
        process(stub)


if __name__ == '__main__':
    print("Enter array containing at least 3 elements "
          "separated by spaces like '1 0 3.4 -4 5' ")
    main()
