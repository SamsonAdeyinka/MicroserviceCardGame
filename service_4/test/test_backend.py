import pytest
import unittest
# from flask_testing import TestCase
from flask import url_for
# import app, db
from application.routes import result
from application.models import Prize_gen

# class TestBase(TestCase):
#     def create_app(self):
#         config_name = 'testing'
#         app.config.update(SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@35.242.157.199/cards_db')
#         return app
#
#     def set_up(self):
#         db.session.commit()
#         db.drop_all()
#         db.create_all()
#
#         query1 = Prize(id="1", Description="hello")
#
#         db.session.add(query1)
#         db.session.commit()
#
#     def tear_down(self):
#         db.session.remove()
#         db.drop_all()

class testApp(TestBase):
    def test_page(self):
        response = self.client.get(url_for('service_4'))
        self.assertEqual(response.status_code, 200)
