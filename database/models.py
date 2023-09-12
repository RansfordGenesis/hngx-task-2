from sqlalchemy import Column, String

from database.database import Base


class Person(Base):
    __tablename__ = "persons"

    name = Column(String)