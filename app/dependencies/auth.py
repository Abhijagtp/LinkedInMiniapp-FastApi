
from fastapi import Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session
from app.dependencies.db import get_db
from app.models.user import User
from app.core.security import SECRET_KEY, ALGORITHM
from jose import jwt, JWTError,ExpiredSignatureError

from fastapi import HTTPException


security = HTTPBearer()


def get_token(crendentials:HTTPAuthorizationCredentials = Depends(security)):
    return crendentials.credentials


def decode_token(token: str):
    try:
        return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

    except ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")

    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")
    

def get_current_user(
    token: str = Depends(get_token),
    db: Session = Depends(get_db)
):
    payload = decode_token(token)

    user_id = payload.get("sub")

    if user_id is None:
        raise HTTPException(status_code=401, detail="Invalid token payload")

    user = db.query(User).filter(User.id == int(user_id)).first()

    if user is None:
        raise HTTPException(status_code=401, detail="User not found")

    return user