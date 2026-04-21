

from app.models.post import Post
from app.models.comment import Comment
from fastapi import HTTPException



def create_comment(db,user_id,post_id,content):
    post = db.query(Post).filter(Post.id == post_id).first()

    if not post:
        raise HTTPException(status_code=404,detail="Post not found")
    

    comment = Comment(
        content=content,
        user_id=user_id,
        post_id=post_id
    
    )

    db.add(comment)
    db.commit()
    db.refresh(comment)


    return comment


def get_comments__for_post(db,post_id):
    return db.query(Comment).filter(Comment.post_id == post_id).all()


def delete_comment(db,comment_id,user_id):
    comment = db.query(Comment).filter(Comment.id == comment_id).first()


    if not comment:
        return HTTPException(status_code=404,detail="Comment not found")
    
    if comment.user_id != user_id:
        return HTTPException(status_code=403,detail="You are not the author of this comment")
    
    db.delete(comment)
    db.commit()
    return comment

