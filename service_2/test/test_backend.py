import pytest
import unittest
# from flask-testing import TestCase
from application.routes import card_points
from flask import url_for
# import app, db

class TestBase(unittest.TestCase):
    def create_app(self):
        config_name = 'testing'
        return

class testApp(unittest.TestBase):
    def test_page(self):
        response = self.client.get(url_for('service_2'))
        self.assertEqual(response.status_code, 200)
