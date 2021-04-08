from flask_testing import TestCase
from flask import url_for
from service3 import app


class TestBase(TestCase):

    def create_app(self):
        return app.app


class TestViews(TestBase):

    def test_index(self):
        response = self.client.get(url_for('createnumber'))
        self.assertEqual(response.status_code, 200)