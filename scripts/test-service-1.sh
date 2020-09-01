cd QA-Lottery/application1
export TEST_DATABASE_URI=mysql+pymysql://root:megabrick55@34.105.176.207:3306/lottery_test_db
pytest --cov applications
