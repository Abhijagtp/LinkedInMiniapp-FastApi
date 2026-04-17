from sqlalchemy import Column, Integer, String,Enum
from sqlalchemy.orm import relationship
from app.db.base import Base
from .enums import UserTypeEnum , UserRole
import enum

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)

    # Relationship with posts
    posts = relationship("Post",back_populates="author")

    role = Column(Enum(UserRole),default=UserRole.USER,nullable=False)
    user_type = Column(Enum(UserTypeEnum),nullable=False)