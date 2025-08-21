from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session,sessionmaker,declarative_base

engine = create_engine('postgresql://user_saksham:5456@localhost/iss_tracking')
db_session = scoped_session(sessionmaker(autocommit=False,
                                          autoflush=False,
                                          bind=engine ))

Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    import Iss_Tracker.models
    Base.metadata.create_all(bind=engine)
