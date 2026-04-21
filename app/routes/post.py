from fastapi import APIRouter, Depends, HTTPException,Query
from sqlalchemy.orm import Session

from app.schemas.post import CreatePostSchema, UpdatePostSchema, PostResponseSchema,PaginatedPostResponse
from app.services.post import (
    create_post as create_post_service,
    get_posts_with_likes,
    get_post_by_id,
    update_post as update_post_service,
    # delete_post
)
from app.dependencies.db import get_db
from app.dependencies.auth import get_current_user
from app.dependencies.roles import require_role, require_user_type

router = APIRouter(prefix="/posts", tags=["Posts"])




@router.post("/create-post",response_model=PostResponseSchema)
def create_post(data:CreatePostSchema,db:Session = Depends(get_db),user = Depends(require_user_type(["teacher"]))):
    post = create_post_service(db,data.title,data.content,author_id=user.id)
    return post

@router.get("/get-posts",response_model=PaginatedPostResponse)
def get_all_posts( 
    db: Session = Depends(get_db),
    user = Depends(get_current_user),
    limit:int= Query(10,ge=1,le=50),
    offset:int = Query(0,ge=0)
                  ):
    
    total,results = get_posts_with_likes(db,user.id,limit,offset)

    return {
        "total":total,
        "posts":results,
        "limit":limit,
        "offset":offset
    }

@router.get("/get-posts/{post_id}",response_model=PostResponseSchema)
def get_post(post_id:int, db:Session = Depends(get_db)):
    post = get_post_by_id(db,post_id)
    if not post:
        raise HTTPException(status_code=404,detail="Post not found")
    return post

@router.put("/update-post/{post_id}",response_model=PostResponseSchema)
def update_post(post_id:int,data:UpdatePostSchema,db:Session = Depends(get_db),user=Depends(get_current_user)):
    post = update_post_service(db,post_id,data.title,data.content,user.id)


    if not post:
        raise HTTPException(status_code=404,detail="Post not found")
    
    if post == "foirbidden":
        raise HTTPException(status_code=403,detail="You are not the author of this post")
    return post


@router.patch("/update-post/{post_id}", response_model=PostResponseSchema)
def patch_post(post_id: int,data: UpdatePostSchema,db: Session = Depends(get_db),user = Depends(get_current_user)):
    post = update_post_service(db, post_id, data.title, data.content)

    if not post:
        raise HTTPException(status_code=404, detail="Post not found")

    return post