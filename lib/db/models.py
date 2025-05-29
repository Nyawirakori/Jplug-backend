from sqlalchemy import Column, Integer, String, Float, DATETIME, ForeignKey, MetaData, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker, relationship


convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)

Base = declarative_base(metadata=metadata)

# Service class
class Service(Base):
    __tablename__ = "services"

    id = Column(Integer(), primary_key=True)
    service_type = Column(String())

    #Relationship
    providers = relationship("Provider", back_populates="service") #Access all providers in a specific service_type

    def __repr__(self):
        return (f"Services offered are {self.service_type}")

    @staticmethod
    def get_services():
        return session.query(Service).all()

# Provider class
class Provider(Base):
    __tablename__ = "providers"

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    location = Column(String())
    phonenumber = Column(String())
    price = Column(Float())
    service_id = Column(Integer(), ForeignKey("services.id"))

    #Relationships
    service = relationship("Service", back_populates="providers")
    bookings = relationship("Booking", back_populates = "provider")

    def __repr__(self):
        return (f"Provider name={self.name}, location={self.location}, phone={self.phonenumber}, price={self.price}")


    @staticmethod
    def get_all():
        return session.query(Provider).all()
    
    @staticmethod
    def find_by_name(name):
        return session.query(Provider).filter(Provider.name ==name).all()

# User class
class User(Base):
    __tablename__ = "users"

    id = Column(Integer(), primary_key = True)
    user_name = Column(String())
    location = Column(String())

    #Relationship
    bookings = relationship("Booking", back_populates="user")

    def __repr__(self):
        return (f"User name is: {self.user_name}, location: {self.location}")
    
    @staticmethod
    def get_users():
        return session.query(User).all()
    
    @staticmethod
    def find_by_user_name(username):
        return session.query(User).filter(User.user_name ==username).all()
  
# Booking class
class Booking(Base):
    __tablename__ = "bookings"

    id = Column(Integer(), primary_key = True)
    created_at = Column(DATETIME())
    status = Column(String())
    user_id = Column(Integer(), ForeignKey("users.id"))
    provider_id = Column(Integer(), ForeignKey("providers.id"))

    #Relationships
    user = relationship("User", back_populates="bookings")
    provider = relationship("Provider", back_populates="bookings")

    def __repr__(self):
        return f"Booking created on {self.created_at} , status is {self.status}"

    @staticmethod
    def get_bookings():
        return session.query(Booking).all()

#creating the engine
engine = create_engine('sqlite:///lib/db/jplug.db')
Session = sessionmaker(bind=engine)
session = Session()