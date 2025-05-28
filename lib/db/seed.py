from models import Service, Booking, Provider, User, Base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from datetime import datetime


engine =create_engine('sqlite:///lib/db/jplug.db')
Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.create_all(engine)

# Clear out old data for a fresh start
session.query(Service).delete()
session.query(Booking).delete()
session.query(User).delete()
session.query(Provider).delete()
session.commit()

#Creating services
s1= Service(service_type= "Plumber")
s2= Service(service_type= "Electrician")

session.add_all([s1, s2])
session.commit()

#Creating users
u1 = User(user_name = "Joan", location ="Nairobi")
u2 = User(user_name = "Kori" ,location ="Mombasa")
u3 = User(user_name = "Mary" ,location ="Embu")
u4 = User(user_name = "Aisha" ,location ="Lamu")
u5 = User(user_name = "Misheck", location ="Nyeri")
u6 = User(user_name = "Darryl" ,location ="Meru")
u7 = User(user_name = "Blair" ,location ="Malindi")

session.add_all([u1, u2, u3, u4, u5, u6, u7])
session.commit()

#creating providers
p1 = Provider(name= "Giveon Zae",location="Nairobi", phonenumber="0712457777", price=2200, service_id=s1.id)
p2= Provider(name= "Brenda Chebet",location="Nairobi", phonenumber="0700111333", price=2300, service_id=s2.id)
p3 = Provider(name= "Ramadan Yusuf",location="Mombasa", phonenumber="0722345678", price=1900, service_id=s1.id)
p4 = Provider(name= "Leila Noor",location="Mombasa", phonenumber="070119988", price=2100, service_id=s2.id)
p5 = Provider(name= "Abdi Hassan",location="Lamu", phonenumber= "0756234567", price= 1700, service_id=s1.id)
p6 = Provider(name= "Halima Bashir",location="Lamu", phonenumber= "0700789012", price=2300, service_id=s2.id)
p7 = Provider(name= "Christine Ndanu",location="Embu", phonenumber="0799887766", price=2000, service_id=s2.id)
p8 = Provider(name= "Andrew Njiru",location="Embu", phonenumber="0700894567", price=1800, service_id=s1.id)
session.add_all([p1, p2,p3,p4,p5,p6,p7,p8])
session.commit()

#creating bookings
b1 = Booking(created_at=datetime.now(), status="Pending", user_id=u1.id, provider_id=p1.id)
b2 = Booking(created_at=datetime.now(), status="Done", user_id=u2.id, provider_id=p3.id)
b3 = Booking(created_at=datetime.now(), status="Done", user_id=u3.id, provider_id=p8.id)

session.add_all([b1, b2, b3])
session.commit()

print("Database Seeded !.")

