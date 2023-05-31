from tg import expose, redirect

from postsapi.lib.base import BaseController
from postsapi.model import User


class AuthController(BaseController):
    @expose('postsapi.templates.login')
    def login(self, **kw):
        user = User().login(kw.get('email'), kw.get('password'))
        if user:
            return redirect('/' + 'posts')
        else:
            return dict(page='login', error='Email ou senha incorretos')

    @expose('postsapi.templates.signup')
    def signup(self, **kw):
        user = User().signup(kw['name'], kw['email'], kw['password'])
        print("user", user)
        if user:
            return redirect('/' + 'posts')
        else:
            return dict(page='signup', error='Campos inválidos')
