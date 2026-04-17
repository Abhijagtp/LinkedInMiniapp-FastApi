from sqlalchemy.orm import Session
from app.models.user import User
from app.core.security import create_access_token,create_refresh_token
from app.models.enums import UserRole,UserTypeEnum

from app.core.security import hash_password
from app.core.security import verify_password



def signup_user(db: Session, email: str, password: str, username: str,user_type:str):
    # 1. Check if user already exists
    role = UserRole.USER

    if role == UserRole.USER and not user_type:
        return {
            "success": False,
            "message": "User type is required for non-user roles"
        }



    existing_user = db.query(User).filter(User.email == email).first()
    if existing_user:
        return {
            "success": False,
            "message": "User already exists"
        }

    # 2. Create new user
    hashed_password = hash_password(password)
    new_user = User(
        username=username,
        email=email,
        password=hashed_password,
        user_type = user_type,
    )

    # 3. Save to DB
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    # 4. Return response
    return {
        "success": True,
        "message": "User created successfully"
    }


def login_user(db: Session, email: str, password: str):
    # 1. Get user from DB
    user = db.query(User).filter(User.email == email).first()

    if not user:
        return {
            "success": False,
            "message": "User not found"
        }

    # 2. Check password
    if not verify_password(password,user.password):
        return {
            "sucess":False,
            "message":"invalid password"
        }

    # 3. Generate fake token (temporary)
    access_token = create_access_token({"sub": str(user.id)})
    refresh_token = create_refresh_token({"sub": str(user.id)})

    return {
        "success": True,
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer"
    }