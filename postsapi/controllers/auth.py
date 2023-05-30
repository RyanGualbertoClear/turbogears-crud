from tg import expose, redirect

from postsapi.lib.base import BaseController
from postsapi.model import Auth


class AuthController(BaseController):
    @expose('postsapi.templates.login')
    def login(self, **kw):
        user = Auth().login(kw['email'], kw['password'])
        if user:
            return redirect('/' + 'post')
        else:
            return dict(page='login', error='Invalid email or password')

    @expose('postsapi.templates.signup')
    def signup(self, **kw):
        user = Auth().signup(kw['name'], kw['email'], kw['password'])
        if user:
            return redirect('/' + 'post')
        else:
            return dict(page='signup', error='Invalid fields')
