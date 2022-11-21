import os
import __main__

from jinja2 import Environment, FileSystemLoader

from .router import Router
from .request import Request
from .template_response import TemplateResponse



class App:
    def __call__(self, env, start_response) -> bytearray:
        method = env['REQUEST_METHOD']
        path = env['PATH_INFO'] or '/'
        callback, url_vars = self.router.match(method, path)

        request = Request(env)        
        response = callback(request, **url_vars)
        start_response(response.status_code, response.header_list)
        if isinstance(response, TemplateResponse):
            return response.render_body(self.jinja2_environment)
        return response.body

    def __init__(self, templates=None) -> None:
        self.router = Router()
        if templates is None:
            # templates = [os.path.join(os.path.abspath('.'), 'templates')]
            templates = [os.path.abspath(os.path.join(__main__.__file__, '..', 'templates'))]
        self.jinja2_environment = Environment(loader=FileSystemLoader(templates))

    def route(self, path=None, method='GET', callback=None):
        def decorator(callback_func):
            self.router.add(method, path, callback_func)
            return callback_func
        return decorator(callback) if callback else decorator

