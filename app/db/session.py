from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://neondb_owner:npg_xaZ0EKnpCj6J@ep-autumn-glade-a16u0zg2-pooler.ap-southeast-1.aws.neon.tech/neondb"

engine = create_engine(DATABASE_URL,pool_pre_ping=True)

SessionLocal = sessionmaker(bind=engine)