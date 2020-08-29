import requests
import unittest

from flask import url_for
from flask_testing import TestCase

from applications import app

class TestBase(TestCase):

    def create_app(self):
        return app

class TestViews(TestBase):

    def test_lottery_view(self):
        """
        Tests that the Lottery page is accessible
        """
        response = self.client.get(url_for('getMyLotteryNumbers'))
        self.assertEqual(response.status_code, 200)

