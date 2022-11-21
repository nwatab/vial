from src.app import App
from wsgiref.simple_server import make_server

app = App()

@app.route('^/$', 'GET')
def hello(request, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain; charset=utf-8')])
    return [b'Hello World']

@app.route('^/user/$', 'POST')
def create_user(request, start_response):
    start_response('201 Created', [('Content-Type', 'text/plain; charset=utf-8')])
    return [b'User Created']

@app.route('^/user/(?P<name>\w+)/$', 'GET')
def user_detail(request, start_response, name):
    start_response('200 OK', [('Content-Type', 'text/plain; charset=utf-8')])
    body = f'Hello {name}'
    return [body.encode('utf-8')]

@app.route('^/user/(?P<name>\w+)/follow/$', 'POST')
def create_user(request, start_response, name):
  start_response('201 Created', [('Content-Type', 'text/plain; charset=utf-8')])
  body = f'Followed {name}'
  return [body.encode('utf-8')]

if __name__ == '__main__':
    httpd = make_server('', 8000, app)
    httpd.serve_forever()