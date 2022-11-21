from app import Router
router = Router()

def create_user():
    return 'user is created'

def user_detail(id):
    return f'user{id} detail'

router.add('POST', '^/users/$', create_user)
router.add('GET', '^/users/(?P<id>\d+)/$', user_detail)

callback, kwargs = router.match('POST', '/users/')
callback(**kwargs)

callback, kwargs = router.match('GET', '/users/1/')
callback(**kwargs)

callback, kwargs = router.match('POST', '/foobar')
callback
dummy_start_response = lambda x, y: print(x, y)

callback({}, dummy_start_response, **kwargs)