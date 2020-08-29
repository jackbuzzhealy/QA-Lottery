import requests
import unittest
from unittest.mock import patch
from flask import url_for, jsonify
from flask_testing import TestCase
from random import randint 
from applications import app

class TestBase(TestCase):

    def create_app(self):
        return app

class TestViews(TestBase):
    def test_LotteryNumbers_view(self):
        """
        Tests that the Lottery Numbers Post page is accessible
        """
        response = self.client.post(url_for('postMyLotteryNumbers'), data="12 49 42 6 41")
        self.assertEqual(response.status_code, 200)

    def test_LighteningBall_view(self):
        """
        Tests that the Lightening Ball Post page is accessible
        """
        response = self.client.post(url_for('postMyLighteningBall'), data="12")
        self.assertEqual(response.status_code, 200)


    def test_LighteningBallWinner_return(self):
        """
        Tests that the lightening ball number is sent, we get another lightening ball
        """
        with patch('random.randint') as p:
            p.return_value = 12
            response = self.client.post(url_for('postMyLighteningBall'), data="12")
            
            self.assertEqual({'match': True, 'winningBall': 12}, response.json)

    def test_LighteningBallLoser_return(self):
        """
        Tests that the lightening ball number is sent, we get another lightening ball
        """
        with patch('random.randint') as p:
            p.return_value = 5
            response = self.client.post(url_for('postMyLighteningBall'), data="12")

            self.assertEqual({'match': False, 'winningBall': 5}, response.json)
