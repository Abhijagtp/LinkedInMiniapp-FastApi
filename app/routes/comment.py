





from fastapi import APIRouter, Depends,HTTPException
from sqlalchemy.orm import Session
from app.schemas.comment import CommentResponseSchema,CreateCommentSchema
from app.dependencies.db import get_db
from app.services.comment import get_comments__for_post,create_comment,delete_comment
from app.dependencies.roles import require_user_type
from app.dependencies.auth import get_current_user



router = APIRouter(prefix="/comments",tags=["Comments"])

@router.get("/{post_id}",response_model = list[CommentResponseSchema])
def get_comment(post_id:int,db:Session = Depends(get_db)):
    return get_comments__for_post(db,post_id)



@router.post("/create-comment/{post_id}",response_model = CommentResponseSchema)
def create_comment_route(post_id:int,
                    data:CreateCommentSchema,
                    user= Depends(require_user_type(["student"])),
                  
                    db:Session = Depends(get_db)):
    print(data)
    comment = create_comment(db,user.id,post_id,data.content)

    if not comment:
        raise HTTPException(status_code=404,detail="Post not found")
    
    return comment

    

@router.delete("/delete-comment/{comment_id}")
def delete_comment_route(
    comment_id:int,
    db:Session = Depends(get_db),
    user= Depends(get_current_user)
):
    
    result = delete_comment(db,comment_id,user.id)

    if result is None:
        raise HTTPException(status_code=404,detail="Comment not found")
    
    if result == "forbidden":
        raise HTTPException(status_code=403,detail="You cant delete this comment")
    
    return {
        "message":"comment deleted successfully"
    }
