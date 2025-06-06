#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.models import Base, Service, Provider, Booking, User, engine

Session = sessionmaker(bind=engine)
session = Session()

if __name__ == '__main__':
    engine = create_engine('sqlite:///lib/db/jplug.db')

    print("Creating database tables if they don't exist...")

    Base.metadata.create_all(engine)
    print("Database table creation process complete.")

    import ipdb; ipdb.set_trace()

   