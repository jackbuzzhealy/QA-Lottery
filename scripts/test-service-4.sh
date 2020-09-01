cd QA-Lottery/application4
pip3 install -r requirements.txt
export DATABASE_URI=mysql+pymysql://root:megabrick55@34.105.176.207:3306/qa_lottery_db
export TEST_DATABASE_URI=mysql+pymysql://root:megabrick55@34.105.176.207:3306/lottery_test_db
pytest --cov applications
