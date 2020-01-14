import pytest
from flask_testing import TestCase
from application.routes import card_points
from flask import url_for
# import app, db

class testApp(TestBase):
    def test_page(self):
        response = self.client.get(url_for('service_2'))
        self.assertEqual(response.status_code, 200)
