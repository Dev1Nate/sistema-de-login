from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, INTEGER, String, Nullable

USUARIO = "root"
SENHA = ""
HOST = "localhost"
BANCO = "exercicio_login"
PORT = 3306
CONN = f'mysql+pymysql://{USUARIO}:{SENHA}@{HOST}:{PORT}/{BANCO}'

engine = create_engine(CONN, echo = False)
Session = sessionmaker(bind = engine)
session = Session()

Base = declarative_base()

class Usuario(Base):
    __tablename__ = "Usuario"
    id = Column(INTEGER,primary_key=True, )
    nome = Column(String(100))
    senha = Column(String(1000), nullable=False)
    email = Column(String(200))
Base.metadata.create_all(engine)



    
