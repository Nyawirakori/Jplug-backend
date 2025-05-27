from sqlalchemy import Column, Integer, String, Float, DATETIME, ForeignKey, MetaData, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker


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

# Provider class
class Provider(Base):
    __tablename__ = "providers"

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    location = Column(String())
    phonenumber = Column(String())
    price = Column(Float())
    service_id = Column(Integer(), ForeignKey("services.id"))

# User class
class User(Base):
    __tablename__ = "users"

    id = Column(Integer(), primary_key = True)
    user_name = Column(String())
    location = Column(String())

# Booking class
class Booking(Base):
    __tablename__ = "bookings"

    id = Column(Integer(), primary_key = True)
    created_at = Column(DATETIME())
    status = Column(String())
    user_id = Column(Integer(), ForeignKey("users.id"))
    provider_id = Column(Integer(), ForeignKey("providers.id"))

#creating the engine
engine = create_engine('sqlite:///lib/db/jplug.db')
Session = sessionmaker(bind=engine)
session = Session()