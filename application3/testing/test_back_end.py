import requests
import unittest

from flask import url_for
from flask_testing import TestCase

from applications import app
     
class TestBase(TestCase):

    def create_app(self):
        return app

class TestViews(TestBase):

    def test_LighteningBall_view(self):
        """
        Tests that the Lightening Ball  page is accessible
        """
        response = self.client.get(url_for('getMyLighteningBall'))
        self.assertEqual(response.status_code, 200)

