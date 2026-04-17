

from sqlalchemy.orm import Session
 
from app.models.post import Post
from app.models.like import Like
from sqlalchemy import func


def create_post(db:Session,title:str,content:str,author_id:int):
    new_post = Post(title=title,content=content,author_id=author_id)
    db.add(new_post)
    db.commit()
    db.refresh(new_post)

    return new_post


def get_posts_with_likes(db):
    results = (
        db.query(
            Post,
            func.count(Like.id).label("like_count")
        )
        .outerjoin(Like, Like.post_id == Post.id)
        .group_by(Post.id)
        .all()
    )

    return results


def get_post_by_id(db:Session,post_id:int):
    return db.query(Post).filter(Post.id == post_id).first()


def update_post(db:Session,post_id:int,title:str,content:str,user_id):
    post = db.query(Post).filter(Post.id == post_id).first() #query to get the user 

    if not post:  # check if post exists
        return None
    
    #check the user ownership of the post 
    if post.author_id != user_id:
        return "foirbidden"

    # update the post
    post.title = title  
    post.content = content


    db.commit()
    db.refresh(post)
    return post


