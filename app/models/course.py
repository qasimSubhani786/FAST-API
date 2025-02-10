from sqlalchemy import Column, Integer, String, Float, Boolean
from app.database.database import Base

class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    price = Column(Float)
    is_early_bird = Column(Boolean, default=None)