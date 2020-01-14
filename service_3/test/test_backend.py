import pytest
from flask import url_for
from app import roll_dice


def test_page(self):
    response = self.client.get(url_for('service_3'))
    self.assertEqual(response.status_code, 200)

def test_roll_dice():
    assert roll_dice() == {'roll': '2'}
