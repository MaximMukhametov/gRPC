import logging
from functools import wraps


logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)


def logging_of_called_rpc_functions(func):
    """Decorator for logging RPC(Remote Procedure Call)"""

    @wraps(func)
    def wrapper(obj, request, context):
        logging.info(f"Request by {context.peer()} "
                     f"called function: '{func.__name__}', "
                     f"with parameter: {request}".rstrip())
        return func(obj, request, context)
    return wrapper
