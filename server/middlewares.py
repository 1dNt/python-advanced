import zlib
from functools import wraps


def comp_middleware(func):
    @wraps(func)
    def wrap(req, *args, **kwargs):
        bytes_req = zlib.decompress(req)
        bytes_resp = func(bytes_req, *args, **kwargs)
        return zlib.compress(bytes_resp)
    return wrap


def decomp_mid_key(func):  # TODO декоратор для функции остановки сервера
    @wraps(func)
    def wrap(resp):
        return func(zlib.decompress(resp))
    return wrap
