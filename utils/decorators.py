import time
from typing import TypeVar, Type, Callable

from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.serializers import Serializer


class log_time:
    def __init__(self, block_name='BLOCK'):
        self.block_name = block_name
        self.start = 0
        self.end = 0

    def __enter__(self, *args, **kwargs):
        self.start = time.time()

    def log(self):
        dtime = self.end - self.start
        print(f'{self.block_name} took {round(dtime, 4)} seconds.')

    def __exit__(self, *args, **kwargs):
        self.end = time.time()
        self.log()

    def __call__(self, f):
        self.block_name = f.__name__

        def wrapped_f(*args, **kwargs):
            self.start = time.time()
            res = f(*args, **kwargs)
            self.end = time.time()
            self.log()
            return res
        wrapped_f.__name__ = f.__name__
        return wrapped_f


T = TypeVar("T")


def parse_request(serializer_class: Type[Serializer], object_class: Type[T]):
    """Parses a request using the serializer class and calls a view function
    with request and deserialized object.
    """
    def view_wrapper(view: Callable[[Request, T], Response]):
        def new_view(request: Request):
            serializer = serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            obj = object_class(**serializer.validated_data)
            return view(request, obj)
        return new_view
    return view_wrapper
