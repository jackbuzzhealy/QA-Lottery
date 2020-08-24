from applications import db
from applications.models import Prizes

db.drop_all()
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
