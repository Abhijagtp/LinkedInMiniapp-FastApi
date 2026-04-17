

from sqlalchemy.orm import Session
 
from app.models.post import Post

def create_post(db:Session,title:str,content:str,author_id:int):
    new_post = Post(title=title,content=content,author_id=author_id)
    db.add(new_post)
    db.commit()
    db.refresh(new_post)

    return new_post


def get_posts(db:Session):
    return db.query(Post).all()


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


