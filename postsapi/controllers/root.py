# -*- coding: utf-8 -*-
"""Main Controller"""

from tg import flash, expose
from tg import tmpl_context
from tg.i18n import ugettext as _
from tg.exceptions import HTTPFound
from postsapi import model
from postsapi.controllers.secure import SecureController
from postsapi.model import DBSession
from tgext.admin.tgadminconfig import BootstrapTGAdminConfig as TGAdminConfig
from tgext.admin.controller import AdminController
from postsapi.lib.base import BaseController
from postsapi.controllers.error import ErrorController
from postsapi.controllers.post import PostController
from postsapi.controllers.auth import AuthController

__all__ = ['RootController']


class RootController(BaseController):
    secc = SecureController()
    admin = AdminController(model, DBSession, config_type=TGAdminConfig)
    post = PostController()
    auth = AuthController()
    error = ErrorController()

    def _before(self):
        tmpl_context.project_name = "postsapi"
        """
        Redirect the user to the initially requested page on logout and say
        goodbye as well.

        """
        flash(_('We hope to see you soon!'))
        return HTTPFound(location='/')

    @expose('postsapi.templates.login')
    def index(self):
        return dict(page='login', error=None)
    
    @expose('postsapi.templates.signup')
    def signup(self):
        return dict(page='signup', error=None)
