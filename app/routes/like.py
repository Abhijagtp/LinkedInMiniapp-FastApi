
from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session
from app.dependencies.db import get_db
from app.dependencies.auth import get_current_user


from app.services.like import toggle_like

router = APIRouter(prefix="/likes",tags=["Likes"])



@router.post("/like-post/{post_id}")
def likepost(post_id:int,
             db:Session = Depends(get_db),
             user = Depends(get_current_user)):
    
    result = toggle_like(db,post_id,user)
    print(result)

    return {"status":result}


@router.get("/get-likes/{post_id}")
def get_like_count(post_id:int,db:Session = Depends(get_db)):
    from app.services.like import get_like_count
    count = get_like_count(db,post_id)
    return {"like_count":count}