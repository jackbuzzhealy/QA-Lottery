#! /bin/bash
cd QA-Lottery

export=DATABASE_URI=mysql+pymysql://root:megabrick55@34.105.176.207:3306/qa_lottery_db
sudo chown jenkins /var/run/docker.sock
sudo chmod 666 /var/run/docker.sock

docker-compose up -d
