import logging

import grpc
from google.rpc import error_details_pb2
from grpc_status import rpc_status

from proto import Request, CalculateMultiplicationStub

_LOGGER = logging.getLogger(__name__)


def process(stub):
    try:
        response = stub.Calculate(Request(array=input()))
        _LOGGER.info('Call success: %.2f', response.result)
    except grpc.RpcError as rpc_error:
        _LOGGER.error('Call failure:\n code: %s \n details: %s',
                      rpc_error.code(),
                      rpc_error.details())
        status = rpc_status.from_call(rpc_error)
        for detail in status.details:
            if detail.Is(error_details_pb2.BadRequest.DESCRIPTOR):
                info = error_details_pb2.BadRequest()
                detail.Unpack(info)
                _LOGGER.error('Bad request: %s', info)
            else:
                raise RuntimeError('Unexpected failure: %s' % detail)


def main():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = CalculateMultiplicationStub(channel)
        process(stub)


if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                        level=logging.INFO)
    print("Enter array containing at least 3 elements "
          "separated by spaces like '1 0 3.4 -4 5' ")
    main()
