from wsgiref.simple_server import make_server

from src.app import App
from src.response import Response

app = App()

@app.route('^/$', 'GET')
def hello(request):
    return Response('Hello World')

@app.route('^/user/$', 'POST')
def create_user(request):
    return Response('User Created', status=201)

@app.route('^/user/(?P<name>\w+)/$', 'GET')
def user_detail(request, name):
    return Response(f'Hello {name}')


if __name__ == '__main__':
    httpd = make_server('', 8000, app)
    httpd.serve_forever()