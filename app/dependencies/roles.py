
from app.dependencies.auth import get_current_user
from fastapi import Depends, HTTPException

from app.models import user



def require_role(allowed_roles:list):
    def role_checker(user=Depends(get_current_user)):
        if user.role not in allowed_roles:
            raise HTTPException(status_code=403,detail="You do not have permission to perform this action")
        return user 
    return role_checker

def require_user_type(allowed_types:list):
    def type_checker(user=Depends(get_current_user)):
        if user.user_type not in allowed_types:
            raise HTTPException(status_code=403,detail="You do not have permission to perform this action")
        return user
    return type_checker



