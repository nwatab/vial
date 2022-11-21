import re

def http404(env, start_response):
    start_response('404 Not Found', [('Content-Type', 'text/plain; charset=utf-8')])
    return [b'404 Not Found']

def http405(env, start_response):
    start_response('405 Method Not Allowed', [('Content-Type', 'text/plain; charset=utf-8')])
    return [b'405 Method Not Allowed']


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
