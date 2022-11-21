import re

from .response import Response

def http404(env):
    return Response(status=404)

def http405(env):
    return Response(status=405)


class Router:
    def __init__(self):
        self.routes = []

    def add(self, method, path, callback):
        self.routes.append({
            'method': method,
            'path': path,
            'callback': callback
        })

    def match(self, method, path):
        error_callback = http404
        for r in self.routes:
            matched = re.compile(r['path']).match(path)
            if not matched:
                continue
            error_callback= http405
            if method == r['method']:
                url_vars = matched.groupdict()
                return r['callback'], url_vars
        return error_callback, {}
