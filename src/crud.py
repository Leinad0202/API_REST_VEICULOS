"""

Aqui fica as configurações e funcionalidades do CRUD (CREATE, READ, UPDATE e DELETE)

"""
from sqlalchemy.orm import Session
from models import Veiculo
from schemas import VeiculoCreate, VeiculoUpdate
from typing import Optional

# CREATE
# db: Session é uma instância para Interagir com o banco durante aquela requisição
# veiculo: VeiculoCreate  é o CRUD chamando os objetos do schemas e repassa com model_dump()
# todo objeto em schemas.py chega no CRUD como dict e precisamos desempacotar

def create_veiculo(db: Session, veiculo: VeiculoCreate):
    db_veiculo = Veiculo(**veiculo.model_dump()) # OBS: model_dump anteriormente utilizado como dict!
    db.add(db_veiculo)
    db.commit()
    db.refresh(db_veiculo)
    return db_veiculo

# READ (listar todos)
def get_veiculos(db: Session, skip: int = 0, limit: int = 100): # faz uma consulta com um limite de 100 resultados
    return db.query(Veiculo).offset(skip).limit(limit).all()


# FILTER (filtragem por ano, marca, placa, modelo e ID)
def filtrar_veiculos(
    db: Session,
    id: Optional[int] = None,
    marca: Optional[str] = None,
    modelo: Optional[str] = None,
    ano: Optional[int] = None,
    placa: Optional[str] = None
):
    query = db.query(Veiculo) # Inicia uma consulta na tabela Veiculo

    if marca:
        query = query.filter(Veiculo.marca.ilike(f"%{marca}%"))
    if modelo:
        query = query.filter(Veiculo.modelo.ilike(f"%{modelo}%"))
    if ano:
        query = query.filter(Veiculo.ano == ano)
    if placa:
        query = query.filter(Veiculo.placa.ilike(f"%{placa}%"))
    if id:
        query = query.filter(Veiculo.id == id)

    return query.all()

# UPDATE
def update_veiculo(db: Session, veiculo_id: int, veiculo_update: VeiculoUpdate): # busca VeiculoUpdate nos schemas e procura o ID do veiculo que você quer atualizar
    db_veiculo = db.query(Veiculo).filter(Veiculo.id == veiculo_id).first() # retorna o primeiro resultado encontrado ou None caso não tenha
    if db_veiculo is None:
        return None
    for var, value in vars(veiculo_update).items(): # vars() retorna um dicionário com os atributos do objeto
        if value is not None:
            setattr(db_veiculo, var, value)
    db.commit()
    db.refresh(db_veiculo)
    return db_veiculo

# DELETE
def delete_veiculo(db: Session, veiculo_id: int): # busca o ID do veiculo que você quer deletar
    db_veiculo = db.query(Veiculo).filter(Veiculo.id == veiculo_id).first() # Busca o arquivo para ser deletado, caso não encontre, retorna None
    if db_veiculo is None:
        return None
    db.delete(db_veiculo)
    db.commit()
    return db_veiculo
