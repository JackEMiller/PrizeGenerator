from flask_testing import TestCase
from flask import url_for
from flask import Flask
from service1 import app, db, Account
import os


class TestBase(TestCase):

    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI=os.getenv('DATABASEURI'),
                SECRET_KEY='TEST_SECRET_KEY',
                DEBUG=True,
                WTF_CSRF_ENABLED=False)
        return app.app
    
    def setUp(self):
        db.create_all()
        sampleuser = Users(account_string="aaaaa",account_int="11111",prize=10)
        db.session.add(sampleuser)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()


class TestViews(TestBase):

    def test_index(self):
        response = self.client.get(url_for('index'))
        self.assertEqual(response.status_code, 200)
