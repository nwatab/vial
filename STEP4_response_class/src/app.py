from .router import Router
from .request import Request


class App:
    def __call__(self, env, start_response) -> bytearray:
        request = Request(env)
        callback, url_vars = self.router.match(request.method, request.path)
        response = callback(request, **url_vars)
        start_response(response.status_code, response.header_list)
        return response.body

    def __init__(self) -> None:
        self.router = Router()

    def route(self, path=None, method='GET', callback=None):
        def decorator(callback_func):
            self.router.add(method, path, callback_func)
            return callback_func
        return decorator(callback) if callback else decorator

