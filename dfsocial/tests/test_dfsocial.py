import unittest

import pytest

from pyramid import testing


class TestDFSocial(unittest.TestCase):
    def test_main_returns_wsgi_app(self):
        from dfsocial import main
        from paste.deploy.loadwsgi import appconfig
        from pyramid.router import Router
        settings = appconfig('config:test.ini', relative_to="./")
        wsgi_ = main({}, **settings)

        assert isinstance(wsgi_, Router)
