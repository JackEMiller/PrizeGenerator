from flask_testing import TestCase
from flask import url_for
from flask import Flask
import service1
import os


class TestBase(TestCase):

    def create_app(self):
        service1.app.app.config.update(SQLALCHEMY_DATABASE_URI=os.getenv('DATABASEURI'),
                SECRET_KEY='TEST_SECRET_KEY',
                DEBUG=True,
                WTF_CSRF_ENABLED=False)
        return app.app
    
    def setUp(self):
        service1.db.create_all()
        sampleuser = service1.Account(account_string="aaaaa",account_int="11111",prize=10)
        service1.db.session.add(sampleuser)
        service1.db.session.commit()

    def tearDown(self):
        service1.db.session.remove()
        service1.db.drop_all()


class TestViews(TestBase):

    def test_index(self):
        response = self.client.get(url_for('index'))
        self.assertEqual(response.status_code, 200)
