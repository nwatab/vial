from wsgiref.simple_server import make_server

from src.app import App
from src.response import Response
from src.template_response import TemplateResponse

app = App()


@app.route('^/user/$', 'GET')
def users(request):
    users = [f'user {i}' for i in range(10)]
    return TemplateResponse('users.html', title='User List', users=users)


if __name__ == '__main__':
    httpd = make_server('', 8000, app)
    httpd.serve_forever()