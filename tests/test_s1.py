from flask_testing import TestCase
from flask import url_for
from flask import Flask
from service1 import app


class TestBase(TestCase):

    def create_app(self):
        return app.app


class TestViews(TestBase):

    def test_index(self):
        response = self.client.get(url_for('index'))
        self.assertEqual(response.status_code, 200)
