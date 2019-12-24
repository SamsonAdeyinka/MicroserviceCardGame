import unittest
from flask import abort, url_for
from flask_testing import TestCase
from os import getenv
from application import app, db
from application.models import Cards

class Testing(TestBase):
    def test_homepage_view(self):
        reponse = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)

    def test_page_1_view(self):
        response = self.client.get(url_for('page-1'))
        self.assertEqual(response.status_code, 200)

    def test_page_2_view(self):
        response = self.client.get(url_for('page-2'))
        self.assertEqual(response.status_code, 200)

    def test_page_3_view(self):
        response = self.client.get(url_for('page-3'))
        self.assertEqual(response.status_code, 200)
