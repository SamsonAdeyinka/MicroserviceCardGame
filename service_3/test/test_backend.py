import pytest
from flask import url_for
from flask_testing import TestCase
import app

class TestBase(TestCase):
    def create_app(self):
        config_name = "testing"
        return app


def test_page(self):
    response = self.client.get(url_for('service_3'))
    self.assertEqual(response.status_code, 200)

# def test_roll_dice():
#     assert roll_dice() == {'roll': '1'}
#
# def test_roll_dice():
#     assert roll_dice() == {'roll': '2'}
#
# def test_roll_dice():
#     assert roll_dice() == {'roll': '3'}
#
# def test_roll_dice():
#     assert roll_dice() == {'roll': '4'}
#
# def test_roll_dice():
#     assert roll_dice() == {'roll': '5'}
#
# def test_roll_dice():
#     assert roll_dice() == {'roll': '6'}
