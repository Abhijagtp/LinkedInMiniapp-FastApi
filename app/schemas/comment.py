
from pydantic import BaseModel
from datetime import datetime



class CreateCommentSchema(BaseModel):
    content : str


class CommentResponseSchema(BaseModel):
    id:int
    content:str
    user_id:int 
    post_id:int
    created_at:datetime

    class Config:
        from_attributes = True