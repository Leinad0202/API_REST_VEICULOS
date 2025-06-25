from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from models import Base  # importa sua classe Base no models.py
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "data", "banco.db")
engine = create_engine(f"sqlite:///{db_path}", echo=True) # cria o banco de dados

SessionLocal = sessionmaker(bind=engine) # Cria uma fábrica de sessões (objetos que representam uma conexão temporária com o banco de dados)

Base.metadata.create_all(engine) # Cria as tabelas no banco de dados a partir das classes declaradas com Base

def get_db():       # get_db é essencial para que o FastAPI consiga injetar a conexão com o banco de dados em cada requisição de forma segura e limpa.
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()