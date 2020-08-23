from applications import db
from applications.models import Prizes

db.drop_all()
db.create_all()

prize1 = TimeSlots(prize=40, no_of_balls=2, lightening_ball="no")
db.session.add(prize1)
prize2 = TimeSlots(prize=25000, no_of_balls=3, lightening_ball="no")
db.session.add(prize2)
prize3 = TimeSlots(prize=600000, no_of_balls=4, lightening_ball="no")
db.session.add(prize3)
prize4 = TimeSlots(prize=2300000, no_of_balls=5, lightening_ball="no")
db.session.add(prize4)
prize5 = TimeSlots(prize=7300000, no_of_balls=6, lightening_ball="no")
db.session.add(prize5)
prize6 = TimeSlots(prize=100, no_of_balls=1, lightening_ball="yes")
db.session.add(prize6)

db.session.commit()
