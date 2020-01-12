import pytest
import unittest
from flask_testing import TestCase
from flask import url_for
import app, db
import application.routes import roll_dice

class TestBase(TestCase):
    def create_app(self):
        config_name = 'testing'
        return

class testApp(TestBase):
    def test_page(self):
        response = self.client.get(url_for('service_2'))
        self.assertEqual(response.status_code, 200)
