import unittest
from router import Router

def create_user():
    return 'user is created'

def user_detail(id):
    return f'user {id} detail'

class RouterTest(unittest.TestCase):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.router = Router()
        self.router.add('POST', '^/users/$', create_user)
        self.router.add('GET', '^/users/(?P<id>\d+)/$', user_detail)

    def test_post(self):
        callback, kwargs = self.router.match('POST', '/users/')
        res = callback(**kwargs)
        self.assertEqual('user is created', res)

    def test_read(self):
        callback, kwargs = self.router.match('GET', '/users/1/')
        res = callback(**kwargs)
        self.assertEqual('user 1 detail', res)

    def test_404(self):
        callback, kwargs = self.router.match('POST', '/foobar')
        dummy_start_response = lambda x, y: (x, y)
        res = callback({}, dummy_start_response, **kwargs)
        self.assertEqual(res, [b'404 Not Found'])
    
    def test_405(self):
        callback, kwargs = self.router.match('DELETE', '/users/1/')
        dummy_start_response = lambda x, y: (x, y)
        res = callback({}, dummy_start_response, **kwargs)
        self.assertEqual(res, [b'405 Method Not Allowed'])


if __name__ == '__main__':
    unittest.main()