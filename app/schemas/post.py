from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from app.schemas.comment import CommentResponseSchema
from typing import List



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
    comments:List[CommentResponseSchema]

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