from app.models.like import Like
from sqlalchemy import func

def toggle_like(db,post_id,user):
    existing = db.query(Like).filter(Like.user_id == user.id, Like.post_id == post_id).first()
    print (existing)

    # agar existing like hai to usko delete kar do (unlike)
    if existing:
        db.delete(existing)
        db.commit()
        return "unliked"
    

    # agar like nahi hai to naya like create kar do
    new_like = Like(user_id=user.id, post_id=post_id)
    db.add(new_like)
    db.commit()
    
    return 'liked'



# get the count of like on the post 

def get_like_count(db,post_id):
    return db.query(func.count(Like.id)).filter(Like.post_id == post_id).scalar()
