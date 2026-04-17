from sqlalchemy import Column, Integer, String, ForeignKey,DateTime
from datetime import datetime
from sqlalchemy.orm import relationship

from app.db.base import Base 


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    content = Column(String)
    author_id = Column(Integer, ForeignKey("users.id"),nullable=False)

    author = relationship("User", back_populates="posts")

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)