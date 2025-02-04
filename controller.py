from COM import Usuario
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, INTEGER, String
from hashlib import sha256

USUARIO = "root"
SENHA = ""
HOST = "localhost"
BANCO = "exercicio_login"
PORT = 3306
CONN = f'mysql+pymysql://{USUARIO}:{SENHA}@{HOST}:{PORT}/{BANCO}'

engine = create_engine(CONN, echo = False)
Session = sessionmaker(bind = engine)
session = Session()

class ControllerUsuario:
    
    def cadastrar_usuario(nome, email, senha):
        criptografada = sha256(senha.encode()).hexdigest()
        x = Usuario(nome=nome, email=email, senha=criptografada)
        
        p1 = session.query(Usuario).all()
        for i in p1:
            if i.email == email:
                return 1 
            
        if len(senha) <= 8 or len(senha) >= 15:
                return 2
        session.add(x)
        session.commit()
        
            
       
    def deletar_usuario(senha, email,):
        p1 = session.query(Usuario).filter(Usuario.email == email)
        x = sha256(senha.encode()).hexdigest()
        for i in p1:
            if i.senha == x:
                deletar = session.query(Usuario).filter(Usuario.email == email and Usuario.senha == senha).delete()
                session.commit()
                return 6
            else:
                return 3
        
        
        
    
    def logar(email, senha,):
        p1 = session.query(Usuario).filter(Usuario.email == email)
        x = sha256(senha.encode()).hexdigest()
        
        for i in p1:
            if i.senha == x:
                return 4
            else:
                return 5
        
x = ControllerUsuario()
#x.cadastrar_usuario(nome = 'davi',email = 'cawfdef', senha = 'sewewewdw')
#x.deletar_usuario(senha='sewewewdw',email='cawfdef')
#x.logar(email='davi@gmail.com', senha='davi1234')

 
       
    