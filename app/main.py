from fastapi import FastAPI

from app.routes import auth
from app.routes import post


app = FastAPI()

app.include_router(auth.router)
app.include_router(post.router)


from app.db.session import engine
from app.db.base import Base
from app.models import user


Base.metadata.create_all(bind=engine)
