
import os
import django
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Set Django settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "my_exam.settings")
django.setup()

# Create SQLAlchemy Database Connection (Use Your MySQL Credentials)
# DATABASE_URL = "mysql+mysqlconnector://root:Dev@1997@localhost/exam_analysis"
DATABASE_URL = "mysql+mysqlconnector://root:Dev%401997@localhost/exam_analysis"


engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
