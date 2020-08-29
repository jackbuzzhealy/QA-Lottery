import requests 
import unittest

from flask import url_for
from flask_testing import TestCase
from unittest.mock import patch

from applications import app, db
from applications.models import Prizes
from os import getenv

class TestBase(TestCase):

    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI='mysql+pymysql://root:megabrick55@34.105.176.207:3306/lottery_test_db',
                SECRET_KEY='gnfdgndkgndflk',
                DEBUG=True
                )
        return app

    def setUp(self):
        """
        Will be called before every test
        """
        # Create table
        db.create_all()
        prize1 = Prizes(prize_value=40, no_of_balls=2, lightening_ball="no")
        db.session.add(prize1)
        prize2 = Prizes(prize_value=25000, no_of_balls=3, lightening_ball="no")
        db.session.add(prize2)
        prize3 = Prizes(prize_value=600000, no_of_balls=4, lightening_ball="no")
        db.session.add(prize3)
        prize4 = Prizes(prize_value=2300000, no_of_balls=5, lightening_ball="no")
        db.session.add(prize4)
        prize5 = Prizes(prize_value=7300000, no_of_balls=6, lightening_ball="no")
        db.session.add(prize5)
        prize6 = Prizes(prize_value=100, no_of_balls=1, lightening_ball="yes")
        db.session.add(prize6)

        db.session.commit()

    def tearDown(self):
        """
        Will be called after every test
        """
        db.session.remove()
        db.drop_all()

class TestViews(TestBase):

    def test_homepage_view(self):
        """
        Testing if homepage is accessible
        """
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)

    def test_lighteningballpage_view(self):
        """
        Testing if the lightening ball page is accessible
        """
        with patch('requests.get') as g:
            with patch('requests.post') as p:
                g.return_value.text = "12"
                p.return_value.text = "6"
                
                response = self.client.get(url_for('generateLighteningBall'))
                self.assertIn(b"12",response.data)
                self.assertIn(b"6",response.data)
                self.assertEqual(response.status_code, 200)
    
    def test_lighteningballpage_prize_winner(self):
        """
        Testing if the lightening ball page gives prize
        """
        with patch('requests.get') as g:
            with patch('requests.post') as p:
                g.return_value.text = "12"
                p.return_value.text = "12"
                
                response = self.client.get(url_for('generateLighteningBall'))
                myNum = response.data
                winningNum = response.data
                prize = 0

                if myNum == winningNum:
                    qry = Prizes.query.filter_by(lightening_ball="yes").first()
                    prize = qry.prize_value
                
                self.assertEqual(prize, 100)
    
    def test_lighteningballpage_lose(self):
        """
        Testing if the lightening ball page gives prize
        """
        with patch('requests.get') as g:
            with patch('requests.post') as p:
                g.return_value.text = "12"
                p.return_value.text = "6"

                myNum = int(g.return_value.text)
                winningNum = int(p.return_value.text)
                prize = 0

                if myNum == winningNum:
                    qry = Prizes.query.filter_by(lightening_ball="yes").first()
                    prize = qry.prize_value

                self.assertEqual(prize, 0)

    def test_lotterypage_view(self):
        """
        Testing if the lottery page is accessible
        """
        fake_json = [{"winningBalls": "6 11 23 19 42 31", "matches": 1}]

        with patch('requests.get') as g:
            with patch('requests.post') as p:
                g.return_value.text = "12 32 21 49 6"
                p.return_value.text.json.return_value = fake_json

                response = self.client.get(url_for('generateLotteryNumbers'))
                self.assertEqual(response.status_code, 200)
                self.assertEqual(response.json(), fake_json)

    def test_lottery_winner(self):
        """
        Testing if the lightening ball page gives prize
        """
        fake_json = [{"winningBalls": "1 2 3 4 5", "matches": 6}]
        with patch('requests.get') as g:
            with patch('requests.post') as p:
                g.return_value.text = "1 2 3 4 5"
                p.return_value.text.json.return_value = fake_json
                
                stringMyNumbers = list(g.return_value.text.split(" "))
                myLotteryNumbers = [int(i) for i in stringNumbers]
                
                stringWinningNumbers = list(p.return_value.text.json.return_value["winningBalls"].split)
                winningNumbers = [int(i) for i in stringWinningNumbers]

                matches = 0
                for ball in myLotteryNumbers:
                    if ball in winningNumbers:
                        matches = matches + 1

                qry = Prizes.query.filter_by(no_of_balls=matches).first()
                prize = qry.prize_value

                self.assertEqual(prize, 7300000)

