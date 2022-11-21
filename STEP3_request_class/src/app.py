from .router import Router
from .request import Request
class App:
    def __call__(self, env, start_response) -> bytearray:
        request = Request(env)
        callback, kwargs = self.router.match(request.method, request.path)
        return callback(request, start_response, **kwargs)

    def __init__(self) -> None:
        self.router = Router()

    def route(self, path=None, method='GET', callback=None):
        def decorator(callback_func):
            self.router.add(method, path, callback_func)
            return callback_func
        return decorator(callback) if callback else decorator

