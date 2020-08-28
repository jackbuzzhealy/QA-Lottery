import requests
import unittest

from flask import url_for
from flask_testing import TestCase

from applications import app

class TestBase(TestCase):

    def create_app(self):
        return app

class TestViews(TestBase):
    def test_LotteryNumbers_view(self):
        """
        Tests that the Lottery Numbers Post page  is accessible
        """
        response = self.client.post(url_for('postMyLotteryNumbers'))
        self.assertEqual(response.status_code, 200)

    def test_LighteningBall_view(self):
        """
        Tests that the Lightening BallPost page  is accessible
        """
        response = self.client.post(url_for('postMyLighteningBall'))
        self.assertEqual(response.status_code, 200)

