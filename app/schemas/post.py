from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class CreatePostSchema(BaseModel):
    title: str
    content: str
    # author_id: int

class PostResponseSchema(BaseModel):
    id: int
    title: str
    content: str
    author_id: int
    created_at: datetime
    like_count: int 
    is_liked:bool

    class Config:
        from_attributes = True

class PaginatedPostResponse(BaseModel):
    total: int
    posts: list[PostResponseSchema]
    limit: int
    offset: int


class PostUpdateRequest(BaseModel):
    id: int
    title: str
    content: str

class UpdatePostSchema(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None