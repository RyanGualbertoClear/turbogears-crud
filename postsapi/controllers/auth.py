from tg import expose, redirect
from postsapi.lib.base import BaseController
from postsapi.model import User


class AuthController(BaseController):
    @expose('postsapi.templates.login')
    def login(self, **kw):
        user = User().login(kw.get('email'), kw.get('password'))
        if user:
            return redirect('/' + 'post')
        else:
            return dict(page='login', error='Email ou senha incorretos')

    @expose('postsapi.templates.signup')
    def signup(self, **kw):
        if not kw.get('name') and not kw.get('email') and not kw.get('password'):
            return dict(page='signup', error='Campos inválidos')

        if kw.get('password') != kw.get('password_confirm'):
            return dict(page='signup', error='Senhas não conferem')

        user = User().signup(kw['name'], kw['email'], kw['password'])
        if user:
            return redirect('/' + 'post')
